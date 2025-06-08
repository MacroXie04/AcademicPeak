from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Q
from index.models import Announcement
from ranking.models import Item
from .serializers import (
    AnnouncementSerializer, AnnouncementCreateUpdateSerializer
)


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the author
        return obj.author == request.user


class AnnouncementViewSet(viewsets.ModelViewSet):
    """
    API endpoint for announcements.
    """
    queryset = Announcement.objects.all()
    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['publish_date', 'priority', 'created_at']
    
    def get_serializer_class(self):
        """Return appropriate serializer class based on action."""
        if self.action in ['create', 'update', 'partial_update']:
            return AnnouncementCreateUpdateSerializer
        return AnnouncementSerializer
    
    def get_queryset(self):
        """
        Filter announcements based on user permissions and publication status.
        """
        queryset = Announcement.objects.all()
        
        # If not staff, only show published announcements that are not expired
        if not self.request.user.is_staff:
            now = timezone.now()
            queryset = queryset.filter(
                Q(is_published=True) &
                (Q(publish_date__lte=now) | Q(publish_date__isnull=True)) &
                (Q(expiry_date__gt=now) | Q(expiry_date__isnull=True))
            )
        
        return queryset
    
    def perform_create(self, serializer):
        """Set the author when creating an announcement."""
        serializer.save(author=self.request.user)


class MainPageViewSet(viewsets.ViewSet):
    """
    API endpoint for the main page data.
    """
    permission_classes = [permissions.AllowAny]
    
    def list(self, request):
        """
        Get data for the main page display.
        """
        # Get featured announcements
        now = timezone.now()
        featured_announcements = Announcement.objects.filter(
            is_published=True,
            featured=True,
            publish_date__lte=now,
            Q(expiry_date__gt=now) | Q(expiry_date__isnull=True)
        ).order_by('-priority', '-publish_date')[:5]
        
        # Get top rated items
        top_items = Item.objects.order_by('-avg_score')[:10]
        
        # Serialize the data
        announcements_data = AnnouncementSerializer(featured_announcements, many=True).data
        
        # For items, we'll use the existing API endpoint
        items_url = request.build_absolute_uri('/api/v1/ranking/items/top_rated/')
        
        return Response({
            'featured_announcements': announcements_data,
            'top_rated_items_url': items_url
        })
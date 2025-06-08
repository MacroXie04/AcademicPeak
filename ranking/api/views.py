from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from ranking.models import Category, Tag, Item, Rating
from .serializers import (
    CategorySerializer, TagSerializer, ItemSerializer, 
    ItemDetailSerializer, ItemCreateUpdateSerializer, RatingSerializer
)


class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow creators of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the creator
        return obj.creator == request.user


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']
    
    def get_permissions(self):
        """Allow anyone to list and retrieve."""
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super().get_permissions()


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint for tags.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']
    
    def get_permissions(self):
        """Allow anyone to list and retrieve."""
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super().get_permissions()


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint for rankable items.
    """
    queryset = Item.objects.all()
    permission_classes = [IsCreatorOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'tags']
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'avg_score', 'score_count', 'created_at']
    
    def get_serializer_class(self):
        """Return appropriate serializer class based on action."""
        if self.action == 'retrieve':
            return ItemDetailSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return ItemCreateUpdateSerializer
        return ItemSerializer
    
    def get_permissions(self):
        """Ensure user is authenticated for create, update, delete."""
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsCreatorOrReadOnly()]
        return [permissions.AllowAny()]
    
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def rate(self, request, pk=None):
        """
        Rate an item.
        """
        item = self.get_object()
        user = request.user
        
        # Check if user has already rated this item
        existing_rating = Rating.objects.filter(item=item, user=user).first()
        
        # Prepare data for serializer
        data = {
            'item': item.id,
            'stars': request.data.get('stars'),
            'review': request.data.get('review', '')
        }
        
        if existing_rating:
            # Update existing rating
            serializer = RatingSerializer(existing_rating, data=data, context={'request': request})
        else:
            # Create new rating
            serializer = RatingSerializer(data=data, context={'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def top_rated(self, request):
        """
        Get top rated items.
        """
        # Get query parameters
        category_id = request.query_params.get('category')
        limit = int(request.query_params.get('limit', 10))
        
        # Filter by category if provided
        queryset = self.get_queryset()
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        
        # Order by average score and limit results
        queryset = queryset.order_by('-avg_score')[:limit]
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class RatingViewSet(viewsets.ModelViewSet):
    """
    API endpoint for ratings.
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['item', 'user', 'stars']
    ordering_fields = ['created_at', 'stars']
    
    def get_queryset(self):
        """
        Filter ratings to show only the user's own ratings or all ratings for admins.
        """
        if self.request.user.is_staff:
            return Rating.objects.all()
        return Rating.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        """Set the user when creating a rating."""
        serializer.save(user=self.request.user)
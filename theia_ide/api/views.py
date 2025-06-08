from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from theia_ide.models import IDEInstance
from .serializers import (
    IDEInstanceSerializer, IDEInstanceCreateSerializer, 
    IDEInstanceActionSerializer
)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the owner
        return obj.user == request.user


class IDEInstanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint for IDE instances.
    """
    queryset = IDEInstance.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    
    def get_serializer_class(self):
        """Return appropriate serializer class based on action."""
        if self.action == 'create':
            return IDEInstanceCreateSerializer
        return IDEInstanceSerializer
    
    def get_queryset(self):
        """
        Filter instances to show only the user's own instances or all instances for admins.
        """
        if self.request.user.is_staff:
            return IDEInstance.objects.all()
        return IDEInstance.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        """Set the user when creating an instance."""
        serializer.save(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def action(self, request, pk=None):
        """
        Perform an action on an IDE instance (start, stop).
        """
        instance = self.get_object()
        serializer = IDEInstanceActionSerializer(data=request.data)
        
        if serializer.is_valid():
            action = serializer.validated_data['action']
            
            if action == 'start' and instance.status == 'stopped':
                # Logic to start the IDE instance
                instance.status = 'running'
                instance.last_accessed_at = timezone.now()
                instance.save()
                return Response({
                    'status': 'success',
                    'message': f'IDE instance {instance.name} started successfully',
                    'access_url': instance.access_url
                })
            
            elif action == 'stop' and instance.status == 'running':
                # Logic to stop the IDE instance
                instance.status = 'stopped'
                instance.save()
                return Response({
                    'status': 'success',
                    'message': f'IDE instance {instance.name} stopped successfully'
                })
            
            else:
                return Response({
                    'status': 'error',
                    'message': f'Cannot {action} IDE instance in {instance.status} state'
                }, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
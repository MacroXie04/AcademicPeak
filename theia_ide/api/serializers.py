from rest_framework import serializers
from django.contrib.auth import get_user_model
from theia_ide.models import IDEInstance

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model (used in nested relationships)."""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class IDEInstanceSerializer(serializers.ModelSerializer):
    """Serializer for IDEInstance model."""
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = IDEInstance
        fields = [
            'id', 'user', 'name', 'description', 'environment_type', 
            'environment_version', 'memory_limit_mb', 'cpu_limit',
            'status', 'access_url', 'container_id', 'last_accessed_at',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['user', 'status', 'access_url', 'container_id', 'last_accessed_at']
    
    def create(self, validated_data):
        """Set the user from the request."""
        validated_data['user'] = self.context['request'].user
        validated_data['status'] = 'creating'  # Initial status
        return super().create(validated_data)


class IDEInstanceCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating an IDEInstance."""
    
    class Meta:
        model = IDEInstance
        fields = [
            'name', 'description', 'environment_type', 
            'environment_version', 'memory_limit_mb', 'cpu_limit'
        ]


class IDEInstanceActionSerializer(serializers.Serializer):
    """Serializer for IDE instance actions (start, stop)."""
    action = serializers.ChoiceField(choices=['start', 'stop'])
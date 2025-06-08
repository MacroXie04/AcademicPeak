from rest_framework import serializers
from django.contrib.auth import get_user_model
from index.models import Announcement

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model (used in nested relationships)."""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class AnnouncementSerializer(serializers.ModelSerializer):
    """Serializer for Announcement model."""
    author = UserSerializer(read_only=True)
    
    class Meta:
        model = Announcement
        fields = [
            'id', 'title', 'content', 'author', 'is_published', 
            'publish_date', 'expiry_date', 'priority', 'featured',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['author']


class AnnouncementCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer for creating and updating Announcement model."""
    
    class Meta:
        model = Announcement
        fields = [
            'title', 'content', 'is_published', 'publish_date', 
            'expiry_date', 'priority', 'featured'
        ]
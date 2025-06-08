from rest_framework import serializers
from django.contrib.auth import get_user_model
from ranking.models import Category, Tag, Item, Rating

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model (used in nested relationships)."""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model."""
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'created_at', 'updated_at']


class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tag model."""
    
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug', 'created_at', 'updated_at']


class RatingSerializer(serializers.ModelSerializer):
    """Serializer for Rating model."""
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Rating
        fields = ['id', 'item', 'user', 'stars', 'review', 'created_at', 'updated_at']
        read_only_fields = ['user']
    
    def create(self, validated_data):
        """Set the user from the request."""
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class ItemSerializer(serializers.ModelSerializer):
    """Serializer for Item model."""
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    creator = UserSerializer(read_only=True)
    
    class Meta:
        model = Item
        fields = [
            'id', 'title', 'slug', 'description', 'category', 'creator',
            'cover', 'avg_score', 'score_count', 'tags', 'created_at', 'updated_at'
        ]
        read_only_fields = ['avg_score', 'score_count', 'creator']
    
    def create(self, validated_data):
        """Set the creator from the request."""
        validated_data['creator'] = self.context['request'].user
        return super().create(validated_data)


class ItemDetailSerializer(ItemSerializer):
    """Detailed serializer for Item model including ratings."""
    ratings = RatingSerializer(many=True, read_only=True)
    
    class Meta(ItemSerializer.Meta):
        fields = ItemSerializer.Meta.fields + ['ratings']


class ItemCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer for creating and updating Item model."""
    
    class Meta:
        model = Item
        fields = ['title', 'slug', 'description', 'category', 'cover', 'tags']
    
    def create(self, validated_data):
        """Set the creator from the request and handle tags."""
        tags_data = validated_data.pop('tags', [])
        validated_data['creator'] = self.context['request'].user
        item = super().create(validated_data)
        
        # Add tags
        if tags_data:
            item.tags.set(tags_data)
        
        return item
    
    def update(self, instance, validated_data):
        """Handle tags when updating."""
        tags_data = validated_data.pop('tags', None)
        item = super().update(instance, validated_data)
        
        # Update tags if provided
        if tags_data is not None:
            item.tags.set(tags_data)
        
        return item
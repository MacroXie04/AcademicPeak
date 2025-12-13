from rest_framework import serializers
from ..models import Menu, Page


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class PageListSerializer(serializers.ModelSerializer):
    menu_title = serializers.CharField(source='menu.name', read_only=True)

    class Meta:
        model = Page
        fields = ['id', 'title', 'slug', 'menu', 'menu_title', 'created_at']


class MenuSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True, read_only=True)
    pages = PageListSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ['id', 'name', 'slug', 'level', 'order', 'children', 'pages']


class PageDetailSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(read_only=True)

    class Meta:
        model = Page
        fields = [
            'id', 'title', 'slug', 'content', 'menu',
            'seo_title', 'seo_description', 'seo_keywords',
            'created_at', 'updated_at'
        ]

from rest_framework import serializers
from content.models import Unit

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'subject', 'title', 'content', 'created_at', 'updated_at']


from rest_framework import serializers
from content.models import Subject
from .unit import UnitSerializer

class SubjectSerializer(serializers.ModelSerializer):
    units = UnitSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = ['id', 'title', 'description', 'units', 'created_at', 'updated_at']


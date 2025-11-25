from rest_framework import viewsets
from content.models import Subject
from content.serializers import SubjectSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


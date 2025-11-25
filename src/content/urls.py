from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, UnitViewSet

router = DefaultRouter()
router.register(r'subjects', SubjectViewSet)
router.register(r'units', UnitViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


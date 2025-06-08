from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnnouncementViewSet, MainPageViewSet

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'announcements', AnnouncementViewSet)
router.register(r'main', MainPageViewSet, basename='main')

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]
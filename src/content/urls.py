from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, PageViewSet

router = DefaultRouter()
router.register(r'menus', MenuViewSet, basename='menu')
router.register(r'pages', PageViewSet, basename='page')

urlpatterns = [
    path('', include(router.urls)),
]

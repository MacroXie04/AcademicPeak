from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserProfileViewSet, WebAuthnCredentialViewSet, UserRegistrationView,
    WebAuthnRegistrationChallengeView, WebAuthnRegistrationCompleteView,
    WebAuthnAuthenticationChallengeView, WebAuthnAuthenticationCompleteView
)

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet)
router.register(r'credentials', WebAuthnCredentialViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='api-register'),
    path('register/challenge/', WebAuthnRegistrationChallengeView.as_view(), name='api-register-challenge'),
    path('register/complete/', WebAuthnRegistrationCompleteView.as_view(), name='api-register-complete'),
    path('auth/challenge/', WebAuthnAuthenticationChallengeView.as_view(), name='api-auth-challenge'),
    path('auth/complete/', WebAuthnAuthenticationCompleteView.as_view(), name='api-auth-complete'),
]
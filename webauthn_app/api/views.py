from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.utils import timezone
from webauthn_app.models import UserProfile, WebAuthnCredential
from .serializers import (
    UserSerializer, UserProfileSerializer, UserRegistrationSerializer,
    WebAuthnCredentialSerializer, WebAuthnRegistrationChallengeSerializer,
    WebAuthnRegistrationCompleteSerializer, WebAuthnAuthenticationChallengeSerializer,
    WebAuthnAuthenticationCompleteSerializer
)

User = get_user_model()


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint for user profiles.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        """
        Filter profiles to show only the user's own profile or all profiles for admins.
        """
        if self.request.user.is_staff:
            return UserProfile.objects.all()
        return UserProfile.objects.filter(user=self.request.user)


class WebAuthnCredentialViewSet(viewsets.ModelViewSet):
    """
    API endpoint for WebAuthn credentials.
    """
    queryset = WebAuthnCredential.objects.all()
    serializer_class = WebAuthnCredentialSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        """
        Filter credentials to show only the user's own credentials or all credentials for admins.
        """
        if self.request.user.is_staff:
            return WebAuthnCredential.objects.all()
        return WebAuthnCredential.objects.filter(user=self.request.user)


class UserRegistrationView(APIView):
    """
    API endpoint for user registration.
    """
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'status': 'success',
                'message': 'User registered successfully. Please complete WebAuthn registration.',
                'user_id': user.id,
                'username': user.username
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WebAuthnRegistrationChallengeView(APIView):
    """
    API endpoint for WebAuthn registration challenge.
    """
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = WebAuthnRegistrationChallengeSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({
                    'status': 'error',
                    'message': 'User not found'
                }, status=status.HTTP_404_NOT_FOUND)
            
            # In a real implementation, generate a challenge and store it in the session
            # For this example, we'll return a mock challenge
            challenge = {
                'challenge': 'mock_challenge_value',
                'rp_id': 'academicpeak.example.com',
                'user_id': str(user.id),
                'username': user.username,
                'timeout': 60000,  # 60 seconds
            }
            
            return Response({
                'status': 'success',
                'challenge': challenge
            })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WebAuthnRegistrationCompleteView(APIView):
    """
    API endpoint for WebAuthn registration completion.
    """
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = WebAuthnRegistrationCompleteSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            credential_id = serializer.validated_data['credential_id']
            public_key = serializer.validated_data['public_key']
            sign_count = serializer.validated_data['sign_count']
            credential_name = serializer.validated_data.get('credential_name', '')
            
            # In a real implementation, verify the attestation and client data
            # For this example, we'll assume verification passed
            
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({
                    'status': 'error',
                    'message': 'User not found'
                }, status=status.HTTP_404_NOT_FOUND)
            
            # Create WebAuthn credential
            WebAuthnCredential.objects.create(
                user=user,
                credential_id=credential_id,
                public_key=public_key,
                sign_count=sign_count,
                credential_name=credential_name,
                last_used_at=timezone.now()
            )
            
            # Activate user
            user.is_active = True
            user.save()
            
            return Response({
                'status': 'success',
                'message': 'WebAuthn registration completed successfully'
            })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WebAuthnAuthenticationChallengeView(APIView):
    """
    API endpoint for WebAuthn authentication challenge.
    """
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = WebAuthnAuthenticationChallengeSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({
                    'status': 'error',
                    'message': 'User not found'
                }, status=status.HTTP_404_NOT_FOUND)
            
            # Get user's credentials
            credentials = WebAuthnCredential.objects.filter(user=user)
            if not credentials.exists():
                return Response({
                    'status': 'error',
                    'message': 'No WebAuthn credentials found for this user'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # In a real implementation, generate a challenge and store it in the session
            # For this example, we'll return a mock challenge
            challenge = {
                'challenge': 'mock_challenge_value',
                'rp_id': 'academicpeak.example.com',
                'timeout': 60000,  # 60 seconds
                'allowed_credentials': [
                    {'id': cred.credential_id, 'type': 'public-key'}
                    for cred in credentials
                ]
            }
            
            return Response({
                'status': 'success',
                'challenge': challenge
            })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WebAuthnAuthenticationCompleteView(APIView):
    """
    API endpoint for WebAuthn authentication completion.
    """
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = WebAuthnAuthenticationCompleteSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            credential_id = serializer.validated_data['credential_id']
            
            # In a real implementation, verify the signature and client data
            # For this example, we'll assume verification passed
            
            try:
                user = User.objects.get(username=username)
                credential = WebAuthnCredential.objects.get(
                    user=user, credential_id=credential_id
                )
            except (User.DoesNotExist, WebAuthnCredential.DoesNotExist):
                return Response({
                    'status': 'error',
                    'message': 'User or credential not found'
                }, status=status.HTTP_404_NOT_FOUND)
            
            # Update credential usage
            credential.last_used_at = timezone.now()
            credential.save()
            
            # In a real implementation, generate a JWT token here
            # For this example, we'll return a mock token
            token = {
                'access': 'mock_access_token',
                'refresh': 'mock_refresh_token'
            }
            
            return Response({
                'status': 'success',
                'message': 'Authentication successful',
                'token': token,
                'user': UserSerializer(user).data
            })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
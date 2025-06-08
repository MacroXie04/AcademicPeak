from rest_framework import serializers
from django.contrib.auth import get_user_model
from webauthn_app.models import UserProfile, WebAuthnCredential

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model."""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active']
        read_only_fields = ['is_active']


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for UserProfile model."""
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'gender', 'profile_img', 'created_at', 'updated_at']
        read_only_fields = ['user']


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    gender = serializers.CharField(required=False, allow_blank=True)
    profile_img = serializers.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name', 'gender', 'profile_img']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    def create(self, validated_data):
        # Remove profile fields from user creation
        gender = validated_data.pop('gender', '')
        profile_img = validated_data.pop('profile_img', None)
        validated_data.pop('password2')
        
        # Create user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            is_active=False  # User is inactive until WebAuthn registration is complete
        )
        
        # Create user profile
        UserProfile.objects.create(
            user=user,
            gender=gender,
            profile_img=profile_img
        )
        
        return user


class WebAuthnCredentialSerializer(serializers.ModelSerializer):
    """Serializer for WebAuthnCredential model."""
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = WebAuthnCredential
        fields = [
            'id', 'user', 'credential_id', 'public_key', 'sign_count',
            'credential_name', 'last_used_at', 'created_at', 'updated_at'
        ]
        read_only_fields = ['user', 'credential_id', 'public_key', 'sign_count', 'last_used_at']


class WebAuthnRegistrationChallengeSerializer(serializers.Serializer):
    """Serializer for WebAuthn registration challenge."""
    username = serializers.CharField(required=True)


class WebAuthnRegistrationCompleteSerializer(serializers.Serializer):
    """Serializer for WebAuthn registration completion."""
    username = serializers.CharField(required=True)
    credential_id = serializers.CharField(required=True)
    public_key = serializers.CharField(required=True)
    sign_count = serializers.IntegerField(required=True)
    credential_name = serializers.CharField(required=False, allow_blank=True)
    client_data = serializers.JSONField(required=True)
    attestation = serializers.JSONField(required=True)


class WebAuthnAuthenticationChallengeSerializer(serializers.Serializer):
    """Serializer for WebAuthn authentication challenge."""
    username = serializers.CharField(required=True)


class WebAuthnAuthenticationCompleteSerializer(serializers.Serializer):
    """Serializer for WebAuthn authentication completion."""
    username = serializers.CharField(required=True)
    credential_id = serializers.CharField(required=True)
    signature = serializers.CharField(required=True)
    client_data = serializers.JSONField(required=True)
    authenticator_data = serializers.CharField(required=True)
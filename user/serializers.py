from django.contrib.auth import get_user_model,authenticate
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""
    class Meta:
        model = get_user_model()
        fields = ['email','password']
        extra_kwargs = {'password':{'write_only':True,'style':{'input_type': 'password'}}}

    def create(self, validated_data):
        """Create a user and return it"""

        return get_user_model().objects.create_user(**validated_data)



class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate user"""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username = email,
            password = password

        )
        if not user:
            message = ("Unable to login")
            raise serializers.ValidationError(message,code='authentication')

        attrs['user'] = user
        return attrs
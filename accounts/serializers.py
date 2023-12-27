from django.contrib.auth.models import User
from rest_framework import serializers


# def clean_email(value):
#     if 'admin' in value:
#         raise serializers.ValidationError('email cant be admin')
#
#
# class UserRegisterSerializer(serializers.Serializer):
#     username = serializers.CharField(required=True)
#     email = serializers.EmailField(required=True, validators=[clean_email])
#     password = serializers.CharField(required=True, write_only=True)
#     password2 = serializers.CharField(required=True, write_only=True)
#
#     def validate_username(self, value):
#         if value == 'admin':
#             raise serializers.ValidationError('username cant be admin')
#         return value
#
#     def validate(self, data):
#         if data['password'] != data['password2']:
#             raise serializers.ValidationError('passwords must match')
#         return data
#
#     def create(self, validated_data):
#         username = validated_data.get('username')
#         email = validated_data.get('email')
#         password = validated_data.get('password')
#         User.objects.create_user(username=username, email=email, password=password)


def clean_email(value):
    if 'admin' in value:
        raise serializers.ValidationError('email cant be admin')


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'email': {'required': True, 'validators': [clean_email]},
            'password': {'required': True, 'write_only': True},
        }

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        User.objects.create_user(username=username, email=email, password=password)

    def validate_username(self, value):
        if value == 'admin':
            raise serializers.ValidationError('username cant be admin')
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('passwords must match')
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        User.objects.create_user(username=username, email=email, password=password)

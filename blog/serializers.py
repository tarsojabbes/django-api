from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "slug", "body", "author", "created_at"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username", "first_name", "last_name", "email", "password"]

    # The create method must be overwriten so the password can ben hashed
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    def update(self, validated_data):
        return User.objects.update(**validated_data)
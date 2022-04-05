from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    class Meta:
        model = Post
        fields = ["id", "title", "slug", "body", "author", "created_at"]

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    class Meta:
        model = User
        fields = ["id","username", "first_name", "last_name", "email", "password", "posts"]

    # The create method must be overwriten so the password can ben hashed
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    def update(self, validated_data):
        return User.objects.update(**validated_data)
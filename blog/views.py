from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from blog.permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, UserSerializer
from .models import Post
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import generics

from rest_framework import generics

class PostList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


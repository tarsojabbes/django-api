from audioop import reverse
from django.contrib.auth.models import User
from rest_framework.response import Response
from blog.permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, UserSerializer
from .models import Post
from rest_framework import permissions
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

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

class PostBody(generics.GenericAPIView):
    queryset = Post.objects.all()
    
    def get(self, request, *args, **kwargs):
        post = self.get_object()
        return Response(post.body)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        "users": reverse("user-list", request=request, format=format),
        "posts": reverse("post-list", request=request, format=format),
    })

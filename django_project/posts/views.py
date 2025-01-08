from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions
from .models import Post
from .permissions import IsAuthorOrReadOnly

from .serializers import PostSerializer
class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)  # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)  # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer
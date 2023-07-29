from django.shortcuts import render
from posts.models import (
    Category,
    SubCategory,
    Post
)
from apis.posts.serializers import (
    CategorySerializer,
    SubCategorySerializer,
    PostSerializer
)
from rest_framework import generics


"""
==========================
        CATEGORY VIEWS
==========================

"""


class ComposerSingleAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ComposerListCreateAPIView(
    generics.ListCreateAPIView
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer





"""
==========================
        POSTS VIEWS
==========================

"""

class PostComposerMixin:
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostListCreateAPIView(PostComposerMixin,generics.ListCreateAPIView):
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user.user_profile)

class PostRetrieveUpdateDestroyAPIView(PostComposerMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


category_list_api_view = ComposerListCreateAPIView.as_view()
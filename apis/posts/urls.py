from django.urls import path
from apis.posts.views import (
    category_list_api_view,
    ComposerSingleAPIView,
    PostListCreateAPIView,
    PostRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path("", PostListCreateAPIView.as_view(), name="post-list-create"),
    path("<int:pk>/", PostRetrieveUpdateDestroyAPIView.as_view()),
    path("categories/",category_list_api_view),
    path("categories/<int:pk>/", ComposerSingleAPIView.as_view()),
]

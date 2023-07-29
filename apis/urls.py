from django.urls import path, include


urlpatterns = [
    path("posts/", include("apis.posts.urls")),
    path("accounts/", include("apis.accounts.urls")),
]


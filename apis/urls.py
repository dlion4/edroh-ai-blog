from django.urls import path, include


urlpatterns = [
    path("posts/", include("apis.posts.urls")),
    path("accounts/", include("apis.accounts.urls")),
    path("essayexpert/", include("apis.essayexpert.urls")),
]



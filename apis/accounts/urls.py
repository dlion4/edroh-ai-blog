from apis.accounts.views import (
    ProfileListCreateAPIView
)
from apis.accounts.auth.views import (
    login,
    signup,
    test_token,
)
from django.urls import path

urlpatterns = [
    path("profiles/", ProfileListCreateAPIView.as_view()),
    path("auth/login/", login),
    path("auth/signup/", signup),
    path("auth/test_token/", test_token),
]

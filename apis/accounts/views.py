from rest_framework import generics
from accounts.models import Profile
from apis.accounts.serializers import (
    ProfileSerializer,
    CustomUserSerializer
)



class ProfileListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()



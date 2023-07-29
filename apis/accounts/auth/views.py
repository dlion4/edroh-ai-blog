from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from apis.accounts.serializers import CustomUserSerializer
from accounts.models import CustomUser


@api_view(["POST", "GET"])
def login(request):
    return Response({"message": "EndPoint Listing for login ..."})


@api_view(["POST"])
def signup(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = CustomUser.objects.get(username=request.data['username'])
        user.set_password(serializer.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})
    return Response({"message": serializer.errors})


@api_view(["GET"])
def test_token(request):
    return Response({"message": "EndPoint Listing for login ..."})

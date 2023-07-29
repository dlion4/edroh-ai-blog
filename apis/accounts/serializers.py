from accounts.models import Profile, CustomUser
from rest_framework import serializers
from posts.models import Post
from apis.posts.serializers import PostSerializer

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = "__all__"
    
    # def create(self, validate_data):
    #     profile_data = 

class ProfileSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ['id','user', 'posts']



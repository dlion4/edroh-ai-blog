from rest_framework import serializers
from posts.models import (
    Category,
    SubCategory,
    Post,
    Comment,
)



    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    author = serializers.ReadOnlyField(source="author.user.username")
    class Meta:
        model = Post
        fields = ["id","author","writer","subcategory","title","content","image","createdAt","updatedAt", "comments"]


class SubCategorySerializer(serializers.ModelSerializer):
    post_category = PostSerializer(many=True)
    class Meta:
        model = SubCategory
        fields = ['category', 'name', 'post_category']



class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id','name', 'subcategories']

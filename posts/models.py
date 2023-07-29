from django.db import models
from accounts.models import Profile

class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)
    
    def __str__(self):
        return str(self.name)
    

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name="subcategories")
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return str(self.name)
    
class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True, related_name="posts")
    writer = models.CharField(max_length=100, help_text="Your Name")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, blank=True, null=True, related_name="post_category")
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    
    def __str__(self):
        return str(self.title)
    
    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = self.title
        return super(Post, self).save(*args, **kwargs)
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.post} comment"
    

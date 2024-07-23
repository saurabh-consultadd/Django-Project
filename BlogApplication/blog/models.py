from django.contrib.auth.models import User
from django.db import models


# class Category(models.Model):
#     name = models.CharField(max_length=250)

#     def __str__(self):
#         return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=50, null=True, editable=False)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    category = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_by = models.CharField(max_length=50, null=True, editable=False)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.comment_by} on {self.post.title}'
        # return f'Comment on {self.post.title}'


# class Users(models.Model):
#     username = models.CharField(max_length=50, unique=True)
#     password = models.CharField(max_length=50)

#     def __str__(self):
#         return self.username
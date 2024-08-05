from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=50, null=True, editable=False)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=50, null=True)
    allow_comments = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment_by = models.CharField(max_length=50, null=True, editable=False)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return f'Comment by {self.comment_by} on {self.post.title}'


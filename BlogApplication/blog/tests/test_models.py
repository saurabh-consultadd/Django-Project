import pytest
from blog.models import Post, Comment

@pytest.mark.django_db
def test_post_str_method():
    post = Post.objects.create(title='Test Post', author='Test Author', body='Test Body')
    assert str(post) == 'Test Post'

@pytest.mark.django_db
def test_comment_str_method():
    post = Post.objects.create(title='Test Post', author='Test Author', body='Test Body')
    comment_by = "admin123"
    comment = Comment.objects.create(post=post, comment_by=comment_by, text='Test Comment')
    assert str(comment) == f'Comment by {comment_by} on {post.title}'

# ---------------------------------------------------------------------------------------------------   
# ---------------------------------------------------------------------------------------------------    

@pytest.mark.django_db
def test_create_post():
    post = Post.objects.create(title='Test Post', author='Test Author', body='Test Body')
    assert post.id is not None

@pytest.mark.django_db
def test_create_comment():
    post = Post.objects.create(title='Test Post', body='Test Body')
    comment = Comment.objects.create(post=post, comment_by="admin123", text='Test Comment')
    assert comment.id is not None



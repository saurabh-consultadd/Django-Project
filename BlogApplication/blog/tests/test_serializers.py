import pytest
from blog.serializer import PostSerializer, CommentSerializer, UserSerializer
from blog.models import Post, Comment
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_post_serializer():
    post_data = {
        'title': 'Test Post',
        'author': 'Test Author',
        'body': 'Test Body',
    }
    post = Post.objects.create(**post_data)
    serializer = PostSerializer(instance=post)

    # Assert serialized data matches the original data
    assert serializer.data['title'] == post_data['title']
    assert serializer.data['author'] == post_data['author']
    assert serializer.data['body'] == post_data['body']

# ---------------------------------------------------------------------------------------------------    

@pytest.mark.django_db
def test_comment_serializer():
    post = Post.objects.create(title='Test Post', author='Test Author', body='Test Body')
    comment_data = {
        'post': post,
        'text': 'Test Comment',
    }
    comment = Comment.objects.create(**comment_data)
    serializer = CommentSerializer(instance=comment)

    # Assert serialized data matches the original data
    assert serializer.data['text'] == comment_data['text']
    assert serializer.data['post'] == post.pk

# ---------------------------------------------------------------------------------------------------    

# @pytest.mark.django_db
# def test_category_serializer():
#     category_data = {
#         'name': 'Test Category',
#     }
#     category = Category.objects.create(**category_data)
#     serializer = CategorySerializer(instance=category)

#     # Assert serialized data matches the original data
#     assert serializer.data['name'] == category_data['name']

# ---------------------------------------------------------------------------------------------------    

@pytest.mark.django_db
def test_user_serializer():
    user_data = {
        'username': 'testuser',
        'password': 'testpassword',
    }
    user = User.objects.create_user(**user_data)
    serializer = UserSerializer(instance=user)

    # Assert serialized data matches the original data
    assert serializer.data['username'] == user_data['username']

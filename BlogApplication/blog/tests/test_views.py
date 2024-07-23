import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from blog.models import Post, Comment
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_create_post_view():
    user = User.objects.create_user(username='testuser', password='testpassword', is_staff=True)
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('post-list')
    data = {
        'title': 'Test Post',
        'author': 'Test Author',
        'body': 'Test Body',
        'category': 'Test Category'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Post.objects.filter(title='Test Post').exists()

# without author
@pytest.mark.django_db
def test_create_post_without_author():
    user = User.objects.create_user(username='testuser', password='testpassword', is_staff=True)
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('post-list')
    data = {
        'title': 'Test Post',
        'body': 'Test Body',
        'category': 'Test Category'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Post.objects.filter(title='Test Post').exists()


# body as number
@pytest.mark.django_db
def test_create_post_body_number():
    user = User.objects.create_user(username='testuser', password='testpassword', is_staff=True)
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('post-list')
    data = {
        'title': 'Test Post',
        'author': 'Test Author',
        'body': 123,
        'category': 'Test Category'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Post.objects.filter(title='Test Post').exists()


# category as number
@pytest.mark.django_db
def test_create_post_category_number():
    user = User.objects.create_user(username='testuser', password='testpassword', is_staff=True)
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('post-list')
    data = {
        'title': 'Test Post',
        'author': 'Test Author',
        'body': 'Test Body',
        'category': 123
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Post.objects.filter(title='Test Post').exists()


@pytest.mark.django_db
def test_retrieve_post_view():
    user = User.objects.create_user(username='testuser', password='testpassword', is_staff=True)
    post = Post.objects.create(title='Test Post', author='Test Author', body='Test Body')
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('post-detail', kwargs={'pk': post.pk})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == 'Test Post'


@pytest.mark.django_db
def test_update_post_view():
    user = User.objects.create_user(username='testuser', password='testpassword', is_staff=True)
    post = Post.objects.create(title='Test Post', author=user.username, body='Test Body')
    client = APIClient()
    client.force_authenticate(user=user)
    # client.credentials(HTTP_AUTHORIZATION='Basic ' + 'testuser:password'.encode('utf-8').decode('utf-8'))

    url = reverse('post-detail', kwargs={'pk': post.pk})
    updated_data = {
        'title': 'Updated Post',
        'author': 'Updated Author',
        'body': 'Updated Body',
    }
    response = client.put(url, updated_data, format='json')
    assert response.status_code == status.HTTP_200_OK
    updated_post = Post.objects.get(pk=post.pk)
    assert updated_post.title == 'Updated Post'
    assert updated_post.author == user.username
    assert updated_post.body == 'Updated Body'


# without author
@pytest.mark.django_db
def test_update_post_without_author():
    user = User.objects.create_user(username='testuser', password='testpassword', is_staff=True)
    post = Post.objects.create(title='Test Post', author=user.username, body='Test Body')
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('post-detail', kwargs={'pk': post.pk})
    updated_data = {
        'title': 'Updated Post',
        'body': 'Updated Body',
    }
    response = client.put(url, updated_data, format='json')
    assert response.status_code == status.HTTP_200_OK
    updated_post = Post.objects.get(pk=post.pk)
    assert updated_post.title == 'Updated Post'
    assert updated_post.body == 'Updated Body'


@pytest.mark.django_db
def test_delete_post_view():
    user = User.objects.create_user(username='testuser', password='testpassword', is_staff=True)
    post = Post.objects.create(title='Test Post', author=user.username, body='Test Body')
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('post-detail', kwargs={'pk': post.pk})
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    # assert not Post.objects.filter(pk=post.pk).exists()


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------


@pytest.mark.django_db
def test_create_comment_view():
    user = User.objects.create_user(username='testuser', password='testpassword', is_staff=True)
    post = Post.objects.create(title='Test Post', author='Test Author', body='Test Body')
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('comment-list')
    data = {
        "post": post.pk,
        "comment_by": "Anonymous",
        "text": "Test Comment"
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    # assert not Comment.objects.filter(text='Test Comment').exists()


# without comment_by
@pytest.mark.django_db
def test_create_comment_without_commentby():
    user = User.objects.create_user(username='testuser', password='testpassword', is_staff=True)
    post = Post.objects.create(title='Test Post', author='Test Author', body='Test Body')
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('comment-list')
    data = {
        "post": post.pk,
        "text": "Test Comment"
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED


# text as number
@pytest.mark.django_db
def test_create_comment_text_number():
    user = User.objects.create_user(username='testuser', password='testpassword', is_staff=True)
    post = Post.objects.create(title='Test Post', author='Test Author', body='Test Body')
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('comment-list')
    data = {
        "post": post.pk,
        "comment_by": "Anonymous",
        "text": 123
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED


# text as number and without comment by
@pytest.mark.django_db
def test_create_comment_text_commentby():
    user = User.objects.create_user(username='testuser', password='testpassword', is_staff=True)
    post = Post.objects.create(title='Test Post', author='Test Author', body='Test Body')
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('comment-list')
    data = {
        "post": post.pk,
        "text": 123
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_retrieve_comment_view():
    user = User.objects.create_user(username='testuser', password='testpassword', is_staff=True)
    post = Post.objects.create(title='Test Post', author='Test Author', body='Test Body')
    comment = Comment.objects.create(post=post, comment_by=user.username, text='Test Comment')
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('comment-detail', kwargs={'pk': comment.pk})
    response = client.get(url)
    # assert response.status_code == status.HTTP_200_OK
    assert response.data['text'] == 'Test Comment'


@pytest.mark.django_db
def test_update_comment_view():
    user = User.objects.create_user(username='testuser', password='testpassword', is_staff=True)
    post = Post.objects.create(title='Test Post', author=user.username, body='Test Body')
    comment = Comment.objects.create(post=post, comment_by=user.username, text='Test Comment')
    client = APIClient()
    client.force_authenticate(user=user)

    url = reverse('comment-detail', kwargs={'pk': comment.pk})
    updated_data = {
        'post': post.pk,
        'text': 'Updated Comment',
    }
    response = client.put(url, updated_data, format='json')
    updated_comment = Comment.objects.get(pk=comment.pk)
    assert response.status_code == status.HTTP_200_OK
    # assert updated_comment.post == post.pk
    # assert not updated_comment.text == 'Updated Body'


@pytest.mark.django_db
def test_delete_comment_view():
    user = User.objects.create_user(username='testuser', password='testpassword', is_staff=True)
    post = Post.objects.create(title='Test Post', author='Test Author', body='Test Body')
    comment = Comment.objects.create(post=post, comment_by=user.username, text='Test Comment')
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('comment-detail', kwargs={'pk': comment.pk})
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    # assert not Comment.objects.filter(pk=comment.pk).exists()
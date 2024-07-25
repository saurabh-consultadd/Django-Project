import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from blog.models import Post, Comment
from django.contrib.auth.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user():
    return User.objects.create(username='testuser', password='password123')

@pytest.mark.django_db
class TestPostViewSet:

    def test_create_post(self, api_client, create_user):
        url = reverse('post-list')
        api_client.force_authenticate(user=create_user)

        data = {
            'title': 'New Post',
            'body': 'New Body Content'
        }
        response = api_client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Post.objects.filter(title='New Post').exists()

    def test_update_post(self, api_client, create_user):
        post = Post.objects.create(title='Test Post', body='Test Body Content', author=create_user)
        url = reverse('post-detail', args=[post.id])
        data = {
            'title': 'Updated Post Title',
            'body': 'Updated Body Content'
        }
        api_client.force_authenticate(user=create_user)
        response = api_client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        post.refresh_from_db()
        assert post.title == 'Updated Post Title'

    def test_delete_post(self, api_client, create_user):
        post = Post.objects.create(title='Test Post', body='Test Body Content', author=create_user)
        url = reverse('post-detail', args=[post.id])
        api_client.force_authenticate(user=create_user)
        response = api_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Post.objects.filter(id=post.id).exists()

    def test_create_post_without_body(self, api_client, create_user):
        url = reverse('post-list')
        api_client.force_authenticate(user=create_user)

        data = {
            'title': 'Test Post Without Body',
        }
        response = api_client.post(url, data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'body' in response.data


    def test_update_post_by_non_author(self, api_client, create_user):
        post = Post.objects.create(title='Test Post', body='Test Body Content', author=create_user)
        url = reverse('post-detail', args=[post.id])
        data = {
            'title': 'Updated Test Post',
            'body': 'Updated Body Content'
        }
        other_user = User.objects.create(username='otheruser', password='password123')
        api_client.force_authenticate(user=other_user)
        response = api_client.put(url, data, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN
        post.refresh_from_db()
        assert post.title != 'Updated Test Post'  # Ensure post title is not updated

    def test_delete_post_by_non_author(self, api_client, create_user):
        post = Post.objects.create(title='Test Post', body='Test Body Content', author=create_user)
        url = reverse('post-detail', args=[post.id])
        # Create a different user
        other_user = User.objects.create(username='otheruser', password='password123')
        api_client.force_authenticate(user=other_user)
        response = api_client.delete(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert Post.objects.filter(id=post.id).exists()


    def test_list_posts(self, api_client, create_user):
        post = Post.objects.create(title='Test Post 1', body='Test Body Content', author=create_user)
        url = reverse('post-list')
        api_client.force_authenticate(user=create_user)

        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['title'] == 'Test Post 1'


    def test_create_post_by_admin(self, api_client):
        admin = User.objects.create(username='otheruser', password='password123', is_staff=True)
        url = reverse('post-list')
        api_client.force_authenticate(user=admin)
        data = {
            'title': 'New Post',
            'body': 'New Body Content'
        }
        response = api_client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Post.objects.filter(title='New Post').exists()

    def test_update_post_by_admin(self, api_client):
        admin = User.objects.create(username='otheruser', password='password123', is_staff=True)
        post = Post.objects.create(title='Test Post', body='Test Body Content', author=admin)
        url = reverse('post-detail', args=[post.id])
        data = {
            'title': 'Updated Test Post',
            'body': 'Updated Body Content'
        }
        api_client.force_authenticate(user=admin)
        response = api_client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        post.refresh_from_db()
        assert post.title == 'Updated Test Post'

    def test_delete_post_by_admin(self, api_client):
        admin = User.objects.create(username='otheruser', password='password123', is_staff=True)
        post = Post.objects.create(title='Test Post', body='Test Body Content', author=admin)
        url = reverse('post-detail', args=[post.id])
        api_client.force_authenticate(user=admin)
        response = api_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Post.objects.filter(id=post.id).exists()


# ------------------------------------------------------------------------------–––––––––––––––––––––––-------
# ------------------------------------------------------------------------------–––––––––––––––––––––––-------
# ------------------------------------------------------------------------------–––––––––––––––––––––––-------


@pytest.mark.django_db
class TestCommentViewSet:

    def test_create_comment(self, api_client, create_user):
        post = Post.objects.create(title='Test Post', body='Test Body Content', author=create_user)
        url = reverse('comment-list')
        api_client.force_authenticate(user=create_user)

        data = {
            'post': post.id,
            'text': 'Test Comment Text'
        }
        response = api_client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Comment.objects.filter(text='Test Comment Text').exists()

    def test_update_comment(self, api_client, create_user):
        post = Post.objects.create(title='Test Post', body='Test Body Content', author=create_user)
        comment = Comment.objects.create(post=post, text='Test Comment', comment_by=create_user)
        url = reverse('comment-detail', args=[comment.id])
        data = {
            'text': 'Updated Comment Text'
        }
        # Create a different user
        other_user = User.objects.create(username='otheruser', password='password123')
        api_client.force_authenticate(user=other_user)
        response = api_client.put(url, data, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN
        comment.refresh_from_db()
        assert comment.text != 'Updated Comment Text'

    def test_delete_comment(self, api_client, create_user):
        post = Post.objects.create(title='Test Post', body='Test Body Content', author=create_user)
        comment = Comment.objects.create(post=post, text='Test Comment', comment_by=create_user)
        url = reverse('comment-detail', args=[comment.id])
        api_client.force_authenticate(user=create_user)
        response = api_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Comment.objects.filter(id=comment.id).exists()


    def test_create_comment_by_author(self, api_client):
        admin = User.objects.create(username='otheruser', password='password123', is_staff=True)
        post = Post.objects.create(title='Test Post', body='Test Body Content', author=admin)
        url = reverse('comment-list')
        api_client.force_authenticate(user=admin)
        data = {
            'post': post.id,
            'text': 'Test Comment Text'
        }
        response = api_client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Comment.objects.filter(text='Test Comment Text').exists()

    def test_update_comment_by_author(self, api_client, create_user):
        admin = User.objects.create(username='otheruser', password='password123', is_staff=True)
        post = Post.objects.create(title='Test Post', body='Test Body Content', author=create_user)
        comment = Comment.objects.create(post=post, text='Test Comment', comment_by=create_user)
        url = reverse('comment-detail', args=[comment.id])
        data = {
            'text': 'Updated Comment Text'
        }
        api_client.force_authenticate(user=admin)
        response = api_client.put(url, data, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN
        comment.refresh_from_db()
        assert not comment.text == 'Updated Comment Text'
    
    def test_delete_comment_by_author(self, api_client, create_user):
        admin = User.objects.create(username='otheruser', password='password123', is_staff=True)
        post = Post.objects.create(title='Test Post', body='Test Body Content', author=admin)
        comment = Comment.objects.create(post=post, text='Test Comment', comment_by=create_user)
        url = reverse('comment-detail', args=[comment.id])
        api_client.force_authenticate(user=admin)
        response = api_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Comment.objects.filter(id=comment.id).exists()


    def test_update_comment_by_non_author(self, api_client, create_user):
        post = Post.objects.create(title='Test Post', body='Test Body Content', author=create_user)
        comment = Comment.objects.create(post=post, text='Test Comment', comment_by=create_user)
        url = reverse('comment-detail', args=[comment.id])
        data = {
            'text': 'Updated Comment Text'
        }
        other_user = User.objects.create(username='otheruser', password='password123')
        api_client.force_authenticate(user=other_user)
        response = api_client.put(url, data, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN
        comment.refresh_from_db()
        assert comment.text != 'Updated Comment Text'

    def test_delete_comment_by_non_author(self, api_client, create_user):
        post = Post.objects.create(title='Test Post', body='Test Body Content', author=create_user)
        comment = Comment.objects.create(post=post, text='Test Comment', comment_by=create_user)
        url = reverse('comment-detail', args=[comment.id])
        # Create a different user
        other_user = User.objects.create(username='otheruser', password='password123')
        api_client.force_authenticate(user=other_user)
        response = api_client.delete(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert Comment.objects.filter(id=comment.id).exists()


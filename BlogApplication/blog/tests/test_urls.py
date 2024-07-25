# blog/tests/test_urls.py
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import PostViewSet, CommentViewSet, user
from rest_framework.routers import DefaultRouter
from django.urls.exceptions import NoReverseMatch

# Initialize the router and register viewsets
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

class TestBlogUrls(SimpleTestCase):

    def test_post_list_url(self):
        url = reverse('post-list')
        self.assertEqual(resolve(url).func.cls, PostViewSet)

    def test_post_detail_url(self):
        url = reverse('post-detail', args=[1])
        self.assertEqual(resolve(url).func.cls, PostViewSet)

    def test_comment_list_url(self):
        url = reverse('comment-list')
        self.assertEqual(resolve(url).func.cls, CommentViewSet)

    def test_comment_detail_url(self):
        url = reverse('comment-detail', args=[1])
        self.assertEqual(resolve(url).func.cls, CommentViewSet)

    def test_user_url(self):
        url = reverse('user')
        self.assertEqual(resolve(url).func, user)

    def test_invalid_method_returns_not_allowed(self):
        url = reverse('post-list')
        response = self.client.put(url)
        self.assertEqual(response.status_code, 405)

    def test_invalid_url_raises_no_reverse_match(self):
        with self.assertRaises(NoReverseMatch):
            reverse('invalid-url')


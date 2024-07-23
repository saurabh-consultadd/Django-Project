from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, user

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
# router.register(r'categories', CategoryViewSet, basename='category')
# router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    # path('register/', RegisterAPI.as_view(), name='register'),
    # path('login/', LoginAPI.as_view(), name='login'),
    path('', include(router.urls)),
    path('user/', user, name='user'),
]

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Post, Comment
from .serializer import PostSerializer, CommentSerializer, UserSerializer

from .permissions import IsPostAuthorOrReadOnly, CanCommentOnPost
from rest_framework.decorators import api_view

import logging

logger = logging.getLogger('blog')


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsPostAuthorOrReadOnly]

    def perform_create(self, serializer):
        logger.info(f'Attempting to create a post with title: {serializer.validated_data["title"]}')
        serializer.save(author=self.request.user.username)
        logger.info(f'Post created: {serializer.instance}')

    def list(self, request):
        logger.info('Listing posts with query params: %s', request.query_params)
        queryset = self.queryset.all().order_by('-created_at')
        # Perform search based on 'search' and 'post_id'
        search_query = request.query_params.get('search', None)
        post_id = request.query_params.get('post_id', None)

        if search_query and search_query.strip():
            logger.debug(f'Searching for posts with query: {search_query}')
            queryset = queryset.filter(title__icontains=search_query) | queryset.filter(author__icontains=search_query) | queryset.filter(category__icontains=search_query)
        if post_id:
            logger.debug(f'Filtering posts by id: {post_id}')
            queryset = queryset.filter(id=post_id)
        serializer = self.serializer_class(queryset, many=True)
        logger.debug(f'Post list query: {queryset.query}')
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        queryset = self.get_object()
        logger.info(f'Attempting to delete post: {queryset.title}')
        self.perform_destroy(queryset)
        logger.info(f'Post deleted: {queryset.title}')
        return Response({"message": f"Post '{queryset.title}' has been deleted."}, status=status.HTTP_204_NO_CONTENT)
    


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CanCommentOnPost]

    def perform_create(self, serializer):
        post = serializer.validated_data['post']
        if not post.allow_comments:
            logger.warning(f'Comment creation denied for post: {post.id} as comments are not allowed.')
            return Response({"detail": "Comments are not allowed for this post."}, status=status.HTTP_403_FORBIDDEN)
        logger.info(f'Creating comment for post: {post.id}')
        serializer.save(comment_by=self.request.user.username)

    def list(self, request):
        logger.info('Listing comments with query params: %s', request.query_params)
        queryset = self.queryset.all()
        # Filter comment based on post_id
        post_id = request.query_params.get('post_id', None)
        if post_id:
            queryset = queryset.filter(post_id=post_id)
        if post_id:
            logger.debug(f'Filtering comments by post id: {post_id}')
            post = Post.objects.filter(id=post_id).first()
            if post and not post.allow_comments:
                logger.warning(f'Comments denied for post: {post_id}')
                return Response({"detail": "Comments are not allowed for this post."}, status=status.HTTP_403_FORBIDDEN)

        parent_comment_id = request.query_params.get('parent_comment_id')
        if parent_comment_id:
            logger.debug(f'Filtering comments by parent comment id: {parent_comment_id}')
            queryset = self.queryset.filter(parent_comment_id=parent_comment_id)
        else:
            queryset = self.queryset.filter(parent_comment__isnull=True)
        serializer = self.serializer_class(queryset, many=True)
        logger.debug(f'Comment list query: {queryset.query}')
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        queryset = self.get_object()
        logger.info(f'Attempting to delete comment: {queryset.text}')
        self.perform_destroy(queryset)
        logger.info(f'Comment deleted: {queryset.text}')
        return Response({"message": f"Comment '{queryset.text}' has been deleted."}, status=status.HTTP_204_NO_CONTENT)
        


@api_view(['POST'])
def user(request):
    logger.info('Creating a new user with data: %s', request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        logger.info(f'User created: {serializer.data}')
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    logger.error(f'User creation failed: {serializer.errors}')
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


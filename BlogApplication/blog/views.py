from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Post, Comment
from .serializer import PostSerializer, CommentSerializer, UserSerializer

from .permissions import IsPostAuthorOrReadOnly, CanCommentOnPost
from rest_framework.decorators import api_view



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsPostAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.username)

    def list(self, request):
        queryset = self.queryset.all().order_by('-created_at')
        # Perform search based on 'search' and 'post_id'
        search_query = request.query_params.get('search', None)
        post_id = request.query_params.get('post_id', None)
        if search_query and search_query.strip():
            queryset = queryset.filter(title__icontains=search_query) | queryset.filter(author__icontains=search_query) | queryset.filter(category__icontains=search_query)
        if post_id:
            queryset = queryset.filter(id=post_id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        queryset = self.get_object()
        self.perform_destroy(queryset)
        return Response({"message": f"Post '{queryset.title}' has been deleted."}, status=status.HTTP_204_NO_CONTENT)
    

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CanCommentOnPost]

    def perform_create(self, serializer):
        post = serializer.validated_data['post']
        if not post.allow_comments:
            return Response({"detail": "Comments are not allowed for this post."}, status=status.HTTP_403_FORBIDDEN)
        serializer.save(comment_by=self.request.user.username)

    def list(self, request):
        queryset = self.queryset.all()
        # Filter comment based on post_id
        post_id = request.query_params.get('post_id', None)
        if post_id:
            queryset = queryset.filter(post_id=post_id)
        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and not post.allow_comments:
                return Response({"detail": "Comments are not allowed for this post."}, status=status.HTTP_403_FORBIDDEN)

        parent_comment_id = request.query_params.get('parent_comment_id')
        if parent_comment_id:
            queryset = self.queryset.filter(parent_comment_id=parent_comment_id)
        else:
            queryset = self.queryset.filter(parent_comment__isnull=True)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        queryset = self.get_object()
        self.perform_destroy(queryset)
        return Response({"message": f"Comment '{queryset.text}' has been deleted."}, status=status.HTTP_204_NO_CONTENT)
        


@api_view(['POST'])
def user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


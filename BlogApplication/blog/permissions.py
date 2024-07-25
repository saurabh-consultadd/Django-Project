from rest_framework.permissions import BasePermission

class IsPostAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only methods
        if request.method in ['GET']:
            return True
        # Allow admin to perform any operations
        if request.user.is_staff:
            return True
        # Allow admin users who created the post to modify or delete it
        return obj.author == request.user.username


class CanCommentOnPost(BasePermission):
    def has_permission(self, request, view):
        # Allow read-only access to comments (GET request)
        if request.method in ['GET']:
            return True
        # Allow admin to perform any operations
        if request.user.is_staff:
            return True
        # Allow any authenticated user to comment (POST request)
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        # Allow permissions to author of the comment or admin
        if request.method in ['PUT', 'PATCH']:
            return obj.comment_by == request.user.username
        # # Allow permissions to author of the post
        # if request.method in ['DELETE']:
        #     return obj.post.author == request.user.username
        if request.method == 'DELETE':
            return obj.comment_by == request.user.username or obj.post.author == request.user.username or request.user.is_staff
        # For GET requests (read-only), allow any authenticated user
        return True

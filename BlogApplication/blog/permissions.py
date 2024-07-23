from rest_framework.permissions import BasePermission

class IsPostAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only methods
        if request.method in ['GET']:
            return True
        # Allow admin users who created the post to modify or delete it
        # if request.user.is_staff and obj.author == request.user:
            # return True
        return obj.author == request.user.username
        # return False


class CanCommentOnPost(BasePermission):
    def has_permission(self, request, view):
        # Allow read-only access to comments (GET request)
        if request.method in ['GET']:
            return True
        # Allow any authenticated user to comment (POST request)
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return request.user and request.user.is_authenticated
        # return obj.comment_by == request.user.username         
        # return False

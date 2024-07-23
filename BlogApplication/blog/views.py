from rest_framework import viewsets, status
# from rest_framework.permissions import AllowAny 
from rest_framework.response import Response
# from rest_framework.views import APIView
from .models import Post, Comment
from .serializer import PostSerializer, CommentSerializer, UserSerializer

from .permissions import IsPostAuthorOrReadOnly, CanCommentOnPost
from rest_framework.decorators import api_view

# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
# from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated



# from .models import Users
# from .serializer import UserSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = Users.objects.all()
#     serializer_class = UserSerializer


# ***************************************************************************************

# class RegisterAPI(APIView):
#     # permission_classes = [AllowAny]
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "User created successfully."})
#         return Response(serializer.errors)
    

# class LoginAPI(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = User.objects.filter(username=username, password=password).exists()
#         if user:
#             return Response({"message": "User login successfully"})
#         else:
#             return Response({"message": "Invalid credentials"})
        
# ***************************************************************************************


# class LoginAPI(APIView):
#     print("heyhhhhh LOGIN")
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = authenticate(username=username, password=password)

#         if user:
#             return Response({"message": "User login successful"})
#         else:
#             return Response({"message": "Invalid credentials"})



# class LoginAPI(APIView):

    
    # def post(self, request):
    #     serializer = LoginSerializer(data=request.data)
    #     if serializer.is_valid():
    #         username=serializer.validate_data['username']
    #         password=serializer.validate_data['password']
    #         user = authenticate(username=username, password=password)

    #         if user:
    #             token, created = Token.objects.get_or_create(user=user)
    #             return Response({
    #                 'message': 'User login successful',
    #                 'token': token.key
    #             })
    #         else:
    #             return Response({'message': 'Invalid credentials'}, status=401)
    #     else:
    #         return Response(serializer.errors, status=400)

            
        #     if user is not None:
        #         token, _ = Token.objects.get_or_create(user=user)
        #         return Response({"token": token.key})
        #     return Response({"message": "Invalid credentials."})
        # return Response(serializer.errors)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsPostAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.username)

    def list(self, request):
        queryset = self.queryset.all()
        # Perform search based on 'search' and 'post_id'
        search_query = request.query_params.get('search', None)
        post_id = request.query_params.get('post_id', None)
        if search_query:
            queryset = queryset.filter(title__startswith=search_query)
        if post_id:
            queryset = queryset.filter(id=post_id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
   
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CanCommentOnPost]

    def perform_create(self, serializer):
        serializer.save(comment_by=self.request.user.username)

    def list(self, request):
        queryset = self.queryset.all()

        # Filter comment based on post_id
        post_id = request.query_params.get('post_id', None)
        if post_id:
            queryset = queryset.filter(post_id = post_id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
        

# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

#     # Endpoint = /categories/1

#     def retrieve(self, request, pk=None):
#         category = self.queryset.filter(pk=pk).first()
#         if not category:
#             return Response({"error": f"Category with id {pk} does not exist."})


@api_view(['POST'])
def user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserViewSet(viewsets.ViewSet):
#     def user(request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def list(self, request):
    #     queryset = User.objects.all()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)
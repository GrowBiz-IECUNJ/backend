from rest_framework import status
from rest_framework.response import Response
from .models import Post, Reply
from .serializers import ForumSerializer, ReplySerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class LoveForumSet(APIView):
    # permission_classes = [IsAuthenticated, ]

    def post(self, request, pk=None):
        post = Post.objects.get(pk=pk)

        if post.likes.contains(request.user):
            post.likes.remove(request.user)
            post.save()

            like = post.likes.count()

            return Response({'detail': 'Post unliked.', "like":  like}, status=status.HTTP_200_OK)
        else:
            post.likes.add(request.user)
            post.save()

            like = post.likes.count()
            return Response({'detail': 'Post liked.', "like":  like}, status=status.HTTP_200_OK)


class ForumViewSet(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = ForumSerializer

    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        self.permission_classes = []
        return super().get(request, *args, **kwargs)

    def post(self, request):
        self.permission_classes = [IsAuthenticated]
        serializer = ForumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReplyViewSet(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]

    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

    def post(self, request, pk=None):
        serializer = ReplySerializer(data=request.data)

        if serializer.is_valid():
            post = Post.objects.get(id=pk)
            reply = serializer.save(post=post, author=request.user)
            return Response(ReplySerializer(reply).data, status=201)
        return Response(serializer.errors, status=400)
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    def patch(self, request, pk):
        try:
            instance = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ForumSerializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
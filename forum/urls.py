from django.urls import path
from .views import ReplyViewSet, ForumViewSet, LoveForumSet, PostDetail


urlpatterns = [
    path('forums/', ForumViewSet.as_view(), name='forum_list'),
    path('forums/<int:pk>/like/', LoveForumSet.as_view(), name='forum_list'),
    path('replies/<int:pk>/create/', ReplyViewSet.as_view(), name='reply_create'),
    path('post/<int:pk>/update/', PostDetail.as_view(), name='umkm-post-update'),
]
from django.urls import path
from .views import CourseListAPIView, LessonListAPIView

urlpatterns = [
    path("courses/", CourseListAPIView.as_view(), name="course-list"),
    path("lessons/<int:id>/", LessonListAPIView.as_view(), name="lessons-id"),
]

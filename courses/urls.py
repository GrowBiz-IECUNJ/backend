from django.urls import path
from .views import (
    CourseListAPIView,
    LessonListAPIView,
    AllLessonsAPIView,
    CourseDetailAPIView,
)

urlpatterns = [
    path("courses/", CourseListAPIView.as_view(), name="course-list"),
    path("courses/<int:id>/", CourseDetailAPIView.as_view(), name="course"),
    path("lessons/", AllLessonsAPIView.as_view(), name="lessons"),
    path("lessons/<int:id>/", LessonListAPIView.as_view(), name="lessons-id"),
]

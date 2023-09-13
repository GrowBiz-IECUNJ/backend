from rest_framework import generics
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class AllLessonsAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class CourseDetailAPIView(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        # Retrieve the course ID from the URL
        course_id = self.kwargs["id"]

        # Get the lessons associated with the specified lesson
        return Course.objects.filter(id=course_id)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        # Retrieve the course ID from the URL
        lesson_id = self.kwargs["id"]

        # Get the lessons associated with the specified lesson
        return Lesson.objects.filter(id=lesson_id)

from rest_framework import generics
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer

class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        # Retrieve the course ID from the URL
        lesson_id = self.kwargs['id']
        
        # Get the lessons associated with the specified lesson
        return Lesson.objects.filter(id=lesson_id)
    
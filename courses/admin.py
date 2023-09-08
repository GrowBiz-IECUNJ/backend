from django.contrib import admin
from .models import Course, Lesson
# from lesson.models import Lesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'photo','get_lesson')
    search_fields = ('name', 'photo')

    def get_lesson(self, object):
        all = []
        get_all_lesson = Lesson.objects.all()
        for lesson in get_all_lesson:
            for lesson1 in object.lesson.all():
                if (lesson1.id == lesson.id):
                    all.append(lesson)
        
        return all

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'creator', 'rating', 'price', 'class_start', 'class_end', 'link_meeting', 'join_status')
    search_fields = ('title', 'creator', 'rating', 'price', 'class_start', 'class_end', 'link_meeting')

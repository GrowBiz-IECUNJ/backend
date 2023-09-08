from django.db import models
    
class Lesson(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='GrowBiz/courses/', default=True)
    description = models.TextField()
    creator = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    class_start = models.DateField()
    class_end = models.DateField()
    total_mentee = models.IntegerField(default=0)
    link_meeting = models.URLField(max_length=200)
    pdf_book = models.URLField(max_length=200)
    join_status = models.BooleanField(default=False) # UMKM should buy this class 

    def __str__(self):
        return self.title
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='GrowBiz/courses/', default=False)
    lesson = models.ManyToManyField(Lesson, blank=False)

    def __str__(self):
        return self.name
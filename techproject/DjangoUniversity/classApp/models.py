from django.db import models


TYPE_CLASSES = {
    ('Intro to Computer Science', 'Intro to Computer Science'),
    ('Python Programming', 'Python Programming'),
    ('App Creation', 'App Creation')
}

class djangoClasses(models.Model):
    title = models.CharField(max_length=60, choices=TYPE_CLASSES)
    course_number = models.IntegerField(default=0)
    instructor_name = models.TextField(max_length=60, default='', blank=True)
    duration = models.FloatField(default=0.00)

    objects = models.Manager()
    def __str__(self):
        return self.title



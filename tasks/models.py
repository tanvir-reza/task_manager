from typing import Any
from django.db import models
from django.contrib.auth.models import User

level = (
    ('High','High'),
    ('Medium','Medium'),
    ('Low','Low'),
)


class Image(models.Model):
    image = models.ImageField(upload_to='task_photos/', verbose_name='Task Photo')

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)




class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False)
    title = models.CharField(max_length=200,blank=False,)
    description = models.TextField(blank=False)
    photos = models.ManyToManyField(Image, blank=True, verbose_name='Task Photos')
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=6,choices=level,default='Low')
    complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
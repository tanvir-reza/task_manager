from typing import Any
from django.db import models
from django.contrib.auth.models import User

level = (
    ('High','High'),
    ('Medium','Medium'),
    ('Low','Low'),
)




class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False)
    title = models.CharField(max_length=200,blank=False,)
    description = models.TextField(blank=False)
    images = models.FileField(upload_to='images/',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(auto_now=False,auto_now_add=False,blank=False)
    priority = models.CharField(max_length=6,choices=level,default='Low')
    complete = models.BooleanField(default=False,blank=False)
    
    def __str__(self):
        return self.title
    



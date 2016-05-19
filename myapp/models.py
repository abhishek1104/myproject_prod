from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime 
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text =  models.TextField(blank=False, null=False)
    created_date = models.DateTimeField(
        default = timezone.now)
    publish_date = models.DateTimeField(
        blank=True,null=True)



    def publish(self): #def means that this is a function/method and publish is the name of the method.
        self.publish_date = timezone.now()
        self.save()


    def approved_comments(self):
        return self.comments.filter(is_approved=True)

    def __str__ (self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey('myapp.Post',related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField (default=timezone.now)
    is_approved = models.BooleanField(default=False)


    def approve(self):
        self.is_approved = True
        self.save()




    def __str__(self):
        self.text




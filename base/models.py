from django.db import models

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


#? create Topics table for my database
class Topic(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return str(self.name)


#! Create your models here.
class Room(models.Model):

    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.CharField(null=True, blank=True, max_length=500)
    #participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return str(self.name)



class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    body = models.TextField()
    updated = models.DateTimeField(auto_now= True)
    created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return str(self.body[:50])

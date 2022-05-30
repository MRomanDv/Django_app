from turtle import update
from django.db import models
from django.contrib.auth.models import User #django in-buil model of User

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name



class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete= models.SET_NULL, null=True)
    name = models.CharField(max_length=200) #like varchar
    description = models.TextField(null = True, blank= True) #this field can be empty/blank
    #participants
    updated = models.DateTimeField(auto_now=True)#this will give us the dateTime of each time call the save method
    created = models.DateTimeField(auto_now_add=True)#This will give us the dateTime only once when this was created

    class Meta:
        ordering = ['-updated', '-created'] #to order the data

    #str representation of the Model
    def __str__(self):
        return self.name

class Message(models.Model):
        user = models.ForeignKey(User,on_delete=models.CASCADE)
        room = models.ForeignKey(Room, on_delete=models.CASCADE)
        body = models.TextField()
        update = models.DateTimeField(auto_now=True)
        created = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.body[0:50] #slicing the first 50 char

        
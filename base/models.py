from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

# Create your models here.


class User(AbstractUser):
    name = models.CharField(unique=True, max_length=60, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(max_length=2000, null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Topic(models.Model):

    # include only name of topic with max_lenght = 40
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Room(models.Model):
    # id by default starts from 1 for every created room
    # User means user id
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # Topic means topic id
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, related_name="participants", blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):

    # has info about user that created, room where message is, body - text of message, update and created date
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.body[:50]

from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_receiver")
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=1000)
    date = models.DateTimeField()


class Conversation(models.Model):
    id = models.AutoField(primary_key=True)
    messages = models.ManyToManyField(Message)
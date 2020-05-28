from django.contrib.auth.models import User
from django.db import models
from map.models import HelpPoint


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_receiver")
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True, blank=True)


class UserInteraction(models.Model):
    """
    Saves the other users a user has communicated with.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="user")
    others = models.ManyToManyField(User, related_name="others")

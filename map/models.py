from django.db import models
from djgeojson.fields import *

# Create your models here.
from djgeojson.fields import PointField
from django.contrib.auth.models import User


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.title}"


class HelpPoint(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    geom = PointField(default="{'type': 'Point', 'coordinates': [0, 0]}")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    @property
    def popupContent(self):
        content = f"""
            {self.title} by {self.author}<br/>
            <a href=/messages/{self.author.id}>Write message</a>
        """
        return content

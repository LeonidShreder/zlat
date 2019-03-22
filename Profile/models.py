from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    users = models.ManyToManyField(User)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


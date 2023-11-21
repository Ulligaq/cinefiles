from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_color = models.CharField(max_length=30)
    favorite_movie = models.CharField(max_length=50)
    age = models.IntegerField(null=True)

    # USERNAME_FIELD = "user"

    def __str__(self):
        return self.user.username

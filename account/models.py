from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.first_name

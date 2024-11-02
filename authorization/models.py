from django.db import models


class Auth(models.Model):
    login = models.CharField(max_length=10)
    password = models.TextField()
from os.path import exists

from django.db import models


class Auth(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    fam = models.CharField(max_length=100)
    login = models.CharField(max_length=10, unique=True)
    password = models.TextField()
    tel = models.CharField(max_length=20)
    email = models.EmailField(default='default@example.com')

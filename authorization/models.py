from os.path import exists

from django.db import models
from django.db.models import CASCADE


class Auth(models.Model):
    user_id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=10, unique=True)
    password = models.TextField()
    tel = models.CharField(max_length=20)
    email = models.EmailField(default='default@example.com')

class Chats(models.Model):
    chat_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    body = models.TextField()
    who_user_id = models.ForeignKey(Auth, on_delete=CASCADE)
    created = models.DateTimeField(auto_now_add=True)
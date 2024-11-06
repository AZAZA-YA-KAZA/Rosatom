from os.path import exists

from django.db import models
from django.db.models import CASCADE


class Auth(models.Model):
    user_id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=10, unique=True)
    password = models.TextField()
    tel = models.CharField(max_length=20)
    email = models.EmailField(default='default@example.com')
    status = models.IntegerField(default=0)

class Chats(models.Model):
    chat_id = models.IntegerField(primary_key=True)
    body = models.TextField()
    otpr_id = models.IntegerField()
    who_user1 = models.ForeignKey(Auth, related_name="on", on_delete=CASCADE)
    who_user2 = models.ForeignKey(Auth, related_name="tw", on_delete=CASCADE)
    created = models.DateTimeField(auto_now_add=True)
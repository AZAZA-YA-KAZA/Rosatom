import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rosatom.settings')  # замените на имя вашего проекта
django.setup()

from authorization.models import *
Auth.objects.create(login='Aswertti', password='q', tel='+79193448376')
Auth.objects.create(login='q', password='q', tel='+78965324245')
Auth.objects.create(login='123', password='123', tel='+78965478522')
Auth.objects.create(login='w', password='w', tel='+79654852142')
root = Auth.objects.get(user_id=1)
a = Auth.objects.get(user_id=2)
b = Auth.objects.get(user_id=3)
c = Auth.objects.get(user_id=4)
d = Auth.objects.get(user_id=5)
Chats.objects.create(otpr_id=1, who_user1=root, who_user2=a)
Chats.objects.create(otpr_id=1, who_user1=root, who_user2=b)
Chats.objects.create(otpr_id=1, who_user1=root, who_user2=c)
Chats.objects.create(otpr_id=1, who_user1=root, who_user2=d)
Chats.objects.create(body='пошли гулять', otpr_id=2, who_user1=b, who_user2=a)
Chats.objects.create(body='я не хочу', otpr_id=3, who_user1=b, who_user2=a)
Chats.objects.create(body='пошли гулять', otpr_id=2, who_user1=c, who_user2=a)
Chats.objects.create(body='нет, ты меня обидел', otpr_id=4, who_user1=c, who_user2=a)
Chats.objects.create(body='пошли гулять', otpr_id=2, who_user1=d, who_user2=a)
Chats.objects.create(body='пошли', otpr_id=5, who_user1=d, who_user2=a)

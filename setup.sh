   echo "Создание миграций..."
   python manage.py makemigrations

   echo "Применение миграций..."
   python manage.py migrate

   echo "Создание пользователя 'root'..."
   python manage.py shell -c "from authorization.models import Auth; Auth.objects.create(login='root', password='root')"

   echo "Настройка завершена!"
   python manage.py runserver

# API атом чата
В ходе разработки проекта учтены следующие требования:
- Регистрация новых пользователей, авторизация;
- Предусмотрена роль модератора, которому доступны все каналы и предоставлена возможность блокировки/разблокировки пользователей;
- Сообщения отправляются в режиме "реального времени";
- Пользователи могут листать свою переписку;
- Проект реализован при помощи Django REST Framework (DRF);

## Запуск проекта
Для автоматической сборки запустите файл setup.sh:
```
   echo "Создание миграций..."
   python manage.py makemigrations

   echo "Применение миграций..."
   python manage.py migrate

   echo "Создание пользователя 'root'..."
   python manage.py shell -c "from authorization.models import Auth; Auth.objects.create(login='root', password='root')"

   echo "Настройка завершена!"
   python manage.py runserver
```
Для создания тестовых данных в консоли введите
```
python testdata.py
```
Создастся 4 пользователя с небольшим диалогом
Проект запущен, можно перейти к самому сайту: http://127.0.0.1:8000/auth/
![image](https://github.com/user-attachments/assets/726a4050-5633-476a-93be-eaeb9cf31379)
По умолчанию создаётся аккаунт модератора:
login - ```root```
password - ``` root```

## Регистрация / авторизация
Помимо авторизации, мы можем зарегистрировать пользователя. Для этого переходим по кнопке `Регистрация`
![image](https://github.com/user-attachments/assets/d0433b91-4726-4e5f-9fd6-dd20c6866ed3)

## Чаты
После решистрации / авторизации, мы переходим к самому чату:
![image](https://github.com/user-attachments/assets/d6af3ed4-fbb1-481a-9b95-356e142b017a)
По умолчанию создаётся диалог `root`. Здесть будут приходит сообщения от модератора.

### Создание чата
Для создания чата нажмите на `Добавить чат` и в окне напишите ник пользователя, с которым хотите начать общение

![image](https://github.com/user-attachments/assets/e7ddc6ed-5737-424d-915a-a106f270cac5)
> [!WARNING]
> Вводить ник надо тот, который зарегистрирован в системе, иначе диалог не создатся, вам выведется соответствующее сообщение.
> Создать диалог с самим собой тоже нельзя.

### Диалог
Сообщения отправляются в режиме реального времени и отображаются в правой части сайта
![image](https://github.com/user-attachments/assets/07203a19-624f-4e13-8174-a28ec17e26f0)
![image](https://github.com/user-attachments/assets/81badf24-b9a6-4ce3-bfc6-4097c78e5507)

### Блокировка
Как упоминалось ранее, модератор в праве блокировать пользователя
![image](https://github.com/user-attachments/assets/dc0e5f0c-700f-41d3-9007-1808f75829fb)
![Снимок экрана 2024-11-06 183532](https://github.com/user-attachments/assets/cbe571c2-14ae-465d-b837-e5151a076980)
После чего пользователю приходит сообщение
![image](https://github.com/user-attachments/assets/1e320653-cc35-4dae-b5a3-6b2467d40d2e)
И поле отправки сообщения, которое находилось у него внизу, уходит. Получается, теперь он может просматривать только диалог
![image](https://github.com/user-attachments/assets/76ad6613-d0a8-440c-a827-2b5dbc05a2e5)

### Выход
Выход из аккаунта производится по кнопке `Выход`, нас опять перекидывает на страницу авторизации.

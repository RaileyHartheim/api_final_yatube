# Проект "API для Yatube"

### API для сервиса блогов "Yatube".

API для Yatube позволяет создавать, редактировать, удалять посты и комментарии к ним,
получать информацию о сообществах и подписываться на других пользователей.

Для реализации проекта использовался Django REST Framework.

### Установка проекта:

- Клонирование репозитория:

```
git clone https://github.com/RaileyHartheim/api_final_yatube.git
cd api_final_yatube/
```

- Cоздание виртуального окружения и его активация

```
python3 -m venv venv
source venv/bin/activate
```

- Установка зависимостей из requirements.txt

```
pip install -r requirements.txt
```

- Выполнение миграций

```
python3 manage.py migrate
```

- Запуск проекта

```
cd yatube_api/
python3 manage.py runserver
```

### Документация к API:

```
http://127.0.0.1:8000/redoc/
```
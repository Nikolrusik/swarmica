# Тестовое Swarmica

Небольшое rest api для библиотеки без авторизации.

## Установка и настройка

Для запуска проекта используйте Docker Compose. Выполните следующую команду:

```bash
docker-compose up -d --build
```

## Локальная разработка
### Для запуска проекта локально без Docker, выполните следующие шаги:

1. Создайте файл .env в корневом каталоге проекта и заполните его необходимыми переменными окружения. Возможно, вам понадобится скопировать .env_docker и внести необходимые изменения.

2. Установите зависимости Python, выполнив команду:

    ```bash
    pip install -r requirements.txt
    ```
3. Запустите локальный сервер с помощью следующей команды:
    ```bash
    python manage.py runserver
    ```
После этого ваш проект будет доступен по адресу http://localhost:8000/.
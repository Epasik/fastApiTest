# Тестовый проект FastAPI + PostgreSQL 

## Описание
Приложение на **FastAPI** с базой данных **PostgreSQL**, упакованное в Docker.

## Требования
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Запуск проекта

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Epasik/fastApiTest.git
   cd <project_folder>
2. Создайте файл .env в корне проекта и укажите переменные окружения:
   ```bash
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_DB=postgres
    POSTGRES_HOST=db
    POSTGRES_PORT=5432

3. Соберите и запустите контейнеры:
   ```bash
   docker-compose up --build
4. Приложение и документация будут доступны по адресам:

   API: http://localhost:8000
   Swagger UI: http://localhost:8000/docs




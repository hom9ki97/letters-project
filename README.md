

# Проект "Отправка писем" с Docker и PostgreSQL

![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 📝 Описание проекта

Данный проект создан в образовательных и тренировочных целях для понимания работы с Docker. Он включает:

- Python-приложение, имитирующее отправку писем различным адресатам
- Базу данных PostgreSQL для хранения информации о пользователях и отправленных письмах
- Docker-контейнеризацию для удобного развертывания

## 🚀 Быстрый старт

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-репозиторий.git
   cd ваш-репозиторий
2. Запустите проект:
   ```bash
   docker compose up
3. Остановите проект:
    ```bash
   docker compose down
   
## 🛠 Технические особенности

1. Логирование: специально оставлено включенным для наглядности работы
2. Задержки вывода: при отключении логов наблюдаются задержки (~30-40 сек) в выводе информации.

## 🔍 Примечания разработчика

Проект создан для изучения:

1. Работы с Docker и Docker Compose
2. Взаимодействия Python-приложений с PostgreSQL
3. Асинхронных операций в Python
4. Логи специально не отключались, чтобы наблюдать процесс работы в реальном времени.

```markdown
<!-- ```mermaid --> 
<!-- graph LR -->
<!--    A[Python App] -->|Сохраняет данные| B[(PostgreSQL)] -->
<!--    A -->|Имитирует отправку| C[Логи писем] -->`
<!-- ``` -->
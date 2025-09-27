Проект для работы с базой данных и управления миграциями с помощью **Alembic**.  
Приложение написано на Python и использует **SQLAlchemy** для ORM, а также удобное CLI-меню для взаимодействия с пользователем.

## 📦 Требования

- Python >= 3.13
- PostgreSQL (для работы с psycopg2)

## 📚 Зависимости

- [alembic](https://alembic.sqlalchemy.org/) — миграции базы данных
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/) — драйвер PostgreSQL
- [python-dotenv](https://pypi.org/project/python-dotenv/) — загрузка переменных окружения из `.env`
- [simple-term-menu](https://pypi.org/project/simple-term-menu/) — удобное терминальное меню
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM для работы с БД
- [tabulate](https://pypi.org/project/tabulate/) — красивый вывод таблиц в консоли

## 🚀 Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/your-username/16-lesson-homework.git
   cd 16-lesson-homework
   ```

2. Установите зависимости:
   ```bash
   uv sync
   ```

3. Создайте файл `.env` на основе примера:
   ```env
   DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/your_database
   ```

4. Примените миграции:
   ```bash
   alembic upgrade head
   ```

## 🛠 Использование

Запуск основного скрипта:
```bash
python main.py
```

Вы получите терминальное меню, через которое можно работать с данными в базе.

## 📂 Структура проекта

```
.
├── alembic/                 # Миграции Alembic
│   └── versions/            # Скрипты миграций
├── core/
│   ├── controller/          # Логика контроллеров
│   └── view/                # Отображение (CLI)
├── models.py                # SQLAlchemy модели
├── main.py                  # Точка входа
├── alembic.ini              # Конфигурация Alembic
├── seed_data.sql            # Первоначальные данные
├── ticket_reservation_service.sql # SQL-скрипт сервиса
├── pyproject.toml           # Конфигурация проекта
└── README.md
```

## 🧾 Лицензия

MIT License. Вы можете свободно использовать и модифицировать этот проект.


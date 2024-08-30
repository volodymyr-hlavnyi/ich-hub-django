from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# Создаем подключение к базе данных
engine = create_engine('mysql+pymysql://root:parhat1994@localhost:3306/data_1')

# Создаем объект MetaData
metadata = MetaData()

# Определяем таблицу (если она еще не существует)
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('email', String(120))
)

# Создаем таблицу в базе данных
metadata.create_all(engine)

# Наполняем таблицу данными
conn = engine.connect()
conn.execute(users.insert(), [
    {'name': 'Иван', 'email': 'ivan@example.com'},
    {'name': 'Мария', 'email': 'maria@example.com'},
    {'name': 'Петр', 'email': 'petr@example.com'}
])
conn.close()

# Теперь используем автоматическое отображение для работы с данными

# Отражаем структуру базы данных
metadata.reflect(bind=engine)

# Создаем базовый класс для автоматического отображения
Base = automap_base(metadata=metadata)

# Подготавливаем базовый класс
Base.prepare()

# Получаем доступ к автоматически созданному классу
User = Base.classes.users

# Создаем сессию и выводим данные
session = Session(engine)
users = session.query(User).all()
for user in users:
    print(f"ID: {user.id}, Имя: {user.name}, Email: {user.email}")

session.close()
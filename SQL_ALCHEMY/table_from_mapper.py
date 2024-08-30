from sqlalchemy import Table, MetaData, Column, Integer, String, create_engine
from sqlalchemy.orm import registry

# Настройка движка и метаданных
engine = create_engine('mysql+pymysql://root:parhat1994@localhost:3306/data_1')
Register = registry()
metadata = MetaData()

# Определение таблицы
user_table = Table('users', metadata,  # Используем metadata напрямую
                   Column('id', Integer, primary_key=True),
                   Column('name', String(255)),
                   Column('age', Integer))

# Определение класса
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Связывание класса с таблицей
Register.map_imperatively(User, user_table)

# Создание таблицы
metadata.create_all(engine)

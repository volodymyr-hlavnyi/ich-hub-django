from sqlalchemy import Table, MetaData, Column, Integer, String, create_engine
from sqlalchemy.orm import mapper, sessionmaker, registry
from sql_alchemy import engine

metadata = MetaData()
Register = registry()

product_table = Table("products1", metadata,
                      Column('id', Integer, primary_key = True),
                      Column('name', String(255)),
                      Column('description', String(225), nullable=True ),
                      Column('price', Integer))

class Product:
    def __init__(self, name , description, price):
        self.name = name
        self.description = description
        self.price = price


user_table = Table("products1", metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String(255)),
                   Column('age', Integer)
                   )

Register.map_imperatively(Product, product_table)

metadata.create_all(engine)
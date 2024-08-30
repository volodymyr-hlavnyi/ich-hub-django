from sqlalchemy import (ForeignKey, Column, Integer, String)
from sql_alchemy import engine, Base
from sqlalchemy.orm import sessionmaker, relationship

Session = sessionmaker(bind=engine)
session = Session()

# Определение моделей
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    children = relationship("Child", back_populates="parent", lazy='joined')

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship("Parent", back_populates="children", uselist = False)

# Создание всех таблиц в базе данных
Base.metadata.create_all(engine)

# Создание нового родителя и детей
new_parent = Parent(name='John')
child1 = Child(name='Anna', parent=new_parent)
child2 = Child(name='Ben', parent=new_parent)

session.add(new_parent)
session.commit()

# Получение родителя и всех его детей одним запросом
parent = session.query(Parent).filter_by(name='John').first()
print(parent.name)
print(child1.parent.name)
print(new_parent.children[0].name)


for child in parent.children:
    print(child.name)

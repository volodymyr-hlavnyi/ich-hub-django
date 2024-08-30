from sqlalchemy import (ForeignKey, Column, Integer, String)
from sql_alchemy import engine, Base
from sqlalchemy.orm import sessionmaker, relationship

Session = sessionmaker(bind=engine)
session = Session()

class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    children = relationship("Child", primaryjoin="Parent.id==Child.parent_id")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey('parent.id'))


# Создание родителя и ребенка
new_parent = Parent(name='John')
child = Child(name='Anna', parent_id=new_parent.id)

session.add(new_parent)
session.add(child)
session.commit()

# Получение родителя с условием соединения
parent = session.query(Parent).filter_by(id=new_parent.id).first()
print(parent.name)
for child in parent.children:
    print(child.name)

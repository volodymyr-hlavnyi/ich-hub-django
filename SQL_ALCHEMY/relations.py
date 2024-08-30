from sqlalchemy import (ForeignKey,
                        Text,
                        Column,
                        Integer,
                        String, Float, Boolean,
                        Table)
from sql_alchemy import engine, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


Session = sessionmaker(bind=engine)
session = Session()


class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    children = relationship("Child", back_populates="parent")


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship("Parent", back_populates="children")

Base.metadata.create_all(engine)


# Создание нового родителя и детей
new_parent = Parent(name='John')
child1 = Child(name='Anna', parent=new_parent)
child2 = Child(name='Ben', parent=new_parent)

# Добавление в сессию и сохранение в базе данных
session.add(new_parent)
session.add(child1)
session.add(child2)
session.commit()

# Получение родителя и связанных с ним детей
parent = session.query(Parent).filter_by(name='John').first()
print(parent.name)
print(new_parent.children[1].name)
# for child in parent.children:
#     print(child.name)

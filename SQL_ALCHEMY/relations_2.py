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
    name = Column(String)
    children = relationship("Child", backref="parent")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey('parent.id'))


# Создание нового родителя и детей
new_parent = Parent(name='John')
child1 = Child(name='Anna')
child2 = Child(name='Ben')

new_parent.children.extend([child1, child2])

# Добавление в сессию и сохранение в базе данных
session.add(new_parent)
session.commit()

# Получение ребенка и его родителя
child = session.query(Child).filter_by(name='Anna').first()
print(child.name)
print(child.parent.name)














from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()
engine = create_engine('sqlite:///database_2.db')
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    addresses = relationship("Address", back_populates="user")


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    description = Column(String(255))
    user = relationship("User", back_populates="addresses")


Base.metadata.create_all(engine)

from datetime import datetime, timedelta


# Добавление пользователей

def create_and_fil_db():
    session.add_all([User(name='Bob', age=22),
                     User(name='David', age=27),
                     User(name='Alice', age=30),
                     User(name='Ann', age=17),
                     User(name='Ann', age=27)])
    session.commit()

    session.add_all([Address(user_id=1, description='New York'),
                     Address(user_id=2, description='London'),
                     Address(user_id=4, description='Berlin')])
    session.commit()


if __name__ == '__main__':
    print('1', '=' * 20)
    name = 'Alice'
    user = session.query(User).filter_by(name=name).first()
    print(f"User: {user.name}, Age: {user.age}")

    print('2', '=' * 20)
    age = 20
    users = session.query(User).filter(User.age > 20).all()
    for user in users:
        print(f"User: {user.name}, Age: {user.age}")

    print('3', '=' * 20)
    userBob = session.query(User).filter_by(name='Bob').first()
    print(f"User: {userBob.name}, Age: {userBob.age}")
    userBob.age = 25
    session.commit()
    print(f"User: {userBob.name}, Age: {userBob.age}")

    print('4', '=' * 20)
    age = 30
    users = session.query(User).filter(User.age < 30).all()
    for user in users:
        print(f"User: {user.name}, Age: {user.age}")

    print('5', '=' * 20)
    name = 'Charlie'
    user = session.query(User).filter_by(name=name).first()
    if user:
        print(f"User is presented: {user.name}, Age: {user.age}")
    else:
        userCharlie = User(name='Charlie', age=35)
        session.add(userCharlie)
        session.commit()
        user = session.query(User).filter_by(name=name).first()
        if user:
            print(f"User creating and now is presented: {user.name}, Age: {user.age}")

    print('6', '=' * 20)
    name = 'Charlie'
    user = session.query(User).filter_by(name=name).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"User deleting: {user.name}, Age: {user.age}")
    else:
        print(f"User not found: {name}")

    print('7', '=' * 20)
    users_sorted_top_4 = session.query(User).order_by(User.age.desc()).limit(4).all()
    for user in users_sorted_top_4:
        print(f"User: {user.name}, Age: {user.age}")

    print('8', '=' * 20)
    users_sored_name = session.query(User).order_by(User.name.asc()).limit(4).all()
    for user in users_sored_name:
        print(f"User: {user.name}, Age: {user.age}")

    print('9', '=' * 20)
    user_id = 5
    new_age = 35
    user = session.query(User).filter_by(id=user_id).first()
    print(f"Before User: {user.name}, Age: {user.age}")
    if user:
        user.age = new_age
        session.commit()
        print(f"After User: {user.name}, Age: {user.age}")

    print('10', '=' * 20)
    name = 'Charlie'
    user = session.query(User).filter_by(name=name).first()
    if user:
        print(f"User exists: {user.name}, Age: {user.age}")
    else:
        print(f"User not found: {name}")

    #11 Django_pr3
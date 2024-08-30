from datetime import datetime

from sqlalchemy import (
    ForeignKey,
    Text,
    Column,
    Integer,
    String,
    Numeric,
    Boolean)
from services import engine, Base
from sqlalchemy.orm import relationship
from pydantic import BaseModel, field_validator, Field, EmailStr


class User(Base):  # declarative style
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    age = Column(Integer, default=18)
    email = Column(String(75), unique=True)


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))
    description = Column(Text)
    city = Column(String(20))
    post_code = Column(Integer, nullable=False, default=111)


# class Parent(Base):
#     __tablename__ = 'parent'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(255))
#     children = relationship("Child", back_populates="parent")
#
#
# class Child(Base):
#     __tablename__ = 'child'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(255))
#     parent_id = Column(Integer, ForeignKey('parent.id'))
#     parent = relationship("Parent", back_populates="children")
#
#
# class Product(Base):
#     __tablename__ = 'product'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(30), nullable=False)
#     price = Column(Numeric(10, 2))
#     in_stock = Column(Boolean)
#     category = relationship('Category', back_populates='products')
#
#
# class Category(Base):
#     __tablename__ = 'category'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(30), nullable=False)
#     description = Column(Text)
#     products = relationship('Product', back_populates='category')


# Создайте модель Event, которая включает поля:
# title (строка),
# date (дата и время события),
# location (строка).
# Добавьте валидацию, чтобы дата события не была в прошлом.
class Event(BaseModel):
    title: str
    date: datetime
    location: str

    @field_validator('date')
    def date_must_be_in_future(cls, v):
        if v < datetime.now():
            raise ValueError('date must be in the future')
        return v


# Определите модель UserProfile с полями:
# username (строка),
# password (строка),
# email (строка с валидацией email).
# Используйте Field для добавления описаний и
# настройки валидации пароля
# (должен быть не менее 8 символов).
class UserProfile(BaseModel):
    username: str
    password: str = Field(..., description='password must be at least 8 characters')
    email: str = EmailStr

    @field_validator('email')
    def email_must_be_valid(cls, v):
        if '@' not in v:
            raise ValueError('invalid email')
        return v

    @field_validator('password')
    def password_must_be_strong(cls, v):
        if len(v) < 8:
            raise ValueError('password must be at least 8 characters')
        return v


Base.metadata.create_all(engine)

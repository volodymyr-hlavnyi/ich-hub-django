from sqlalchemy import Column, Integer, String, Numeric, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from hw.hw_3.connect2memory import engine
from hw.hw_3.connect2memory import Base


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Numeric(10, 2))
    in_stock = Column(Boolean)

    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship("Category", back_populates="products")


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))

    products = relationship("Product", back_populates="category")



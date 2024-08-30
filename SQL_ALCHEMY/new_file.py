from sqlalchemy import (ForeignKey,
                        Text,
                        Column,
                        Integer,
                        String, Float, Boolean,
                        Table)
from sql_alchemy import engine, Base
from sqlalchemy.orm import relationship

tags_association = Table(
    'tags_association',
    Base.metadata,
    Column('product_id', Integer, ForeignKey("product.id")),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(15), nullable=False)
    price = Column(Float)
    available = Column(Boolean)
    tags = relationship('Tag',
                        secondary=tags_association,
                        back_populates='products')

class Tag(Base):
    __tablename__ = "tag"
    id = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False)
    products = relationship('Product',
                            secondary=tags_association,
                            back_populates='tags')

Base.metadata.create_all(engine)











# # Создание продукта
# product = Product(name="Телефон", price=999.99, available=True)
#
# # Создание тега
# tag = Tag(name="Электроника")
#
# # Связывание продукта и тега
# product.tags.append(tag)
# # или
# tag.products.append(product)
#
# # Теперь вы можете обращаться к связанным объектам
# print(product.tags)  # Выведет список тегов для продукта
# print(tag.products)  # Выведет список продуктов с этим тегом
from sqlalchemy import (ForeignKey,
                        Text,
                        Column,
                        Integer,
                        String, Float, Boolean,
                        Table)
from sql_alch import engine, Base
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

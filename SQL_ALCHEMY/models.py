from sqlalchemy import ForeignKey, Text, Column, Integer, String
from sql_alchemy import engine, Base


class User(Base):  #declarative style
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    age = Column(Integer, nullable= False)
    email = Column(String(75), unique=True)



class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete= "CASCADE"))
    description = Column(Text)
    city = Column(String(20))
    post_code = Column(Integer, nullable = False, default = 111)





Base.metadata.create_all(engine)
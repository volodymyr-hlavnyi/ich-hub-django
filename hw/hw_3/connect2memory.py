from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:')  # , echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


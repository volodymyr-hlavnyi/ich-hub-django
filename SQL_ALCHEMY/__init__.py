from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base



engine = create_engine('mysql+pymysql://root:parhat1994@localhost:3306/data_1')

Base = declarative_base()

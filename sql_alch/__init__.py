from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.testing.plugin.plugin_base import engines

engine = create_engine('sqlite:///examples.db')
# engine = create_engine('mysql+pymysql://root:parhat1994@localhost:3306/data_1')
# engine = (
#      create_engine(
#          'mysql+pymysql://ich1:ich1_password_ilovedbs@mysql.itcareerhub.de:3306/310524ptm_Volodymyr'))

Base = declarative_base()




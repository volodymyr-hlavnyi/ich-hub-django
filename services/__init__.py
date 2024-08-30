from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import logging


engine = create_engine('sqlite:///db/examples.db')
# engine = create_engine('mysql+pymysql://root:parhat1994@localhost:3306/data_1')
# engine = (
#      create_engine(
#      'mysql+pymysql://ich1:ich1_password_ilovedbs@ich-edit.edu.itcareerhub.de:3306/310524ptm_Volodymyr_alchemy'
#      )
#      )

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.INFO)

Base = declarative_base()




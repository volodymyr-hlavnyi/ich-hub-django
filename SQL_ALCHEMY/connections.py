from sqlalchemy.orm import sessionmaker
from sql_alchemy import engine
from models import User, Address
import logging



logging.basicConfig(level = logging.INFO)
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.INFO)


Session = sessionmaker(bind=engine)
session = Session()


# user1 = User(
#     name = 'Patrick',
#
#     age = 56,
#     email = 'vladafds@gmail.com'
# )


# user3 = User(
#     name = 'Spomge',
#     surname = 'Bob',
#     age = 59,
#     email = 'bob@yahoo.com'
# )

# address1 = Address(
#     user_id = 1,
#     description = 'Apartment',
#     city = "LA"
# )

#
# session.add(user1)
# session.commit()

user = session.query(User).filter(User.id == 1).first()
session.delete(user)
session.commit()

session.close()

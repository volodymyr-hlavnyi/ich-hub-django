from datetime import datetime, timedelta

from sqlalchemy.orm import sessionmaker
from sql_alch import engine
from models import User, Address, Parent, Child, Event, Product, Category, UserProfile
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.INFO)

Session = sessionmaker(bind=engine)
session = Session()


def create_user_address():
    user1 = User(
        name='John',
        age=25,
        email='john@expale.com')

    address1 = Address(
        description='address 1',
        city='New York',
        post_code=1234558678,
        user_id=1)

    session.add(user1)
    session.add(address1)
    session.commit()
    session.close()


def delete_user_address():
    user_data = session.query(User).filter(User.id == 1).first()
    session.delete(user_data)
    address_data = session.query(Address).filter(Address.id == 1).first()
    session.delete(address_data)
    session.commit()
    session.close()


def create_parent_child():
    parent = Parent(name='parent1')
    child = Child(name='child1', parent=parent)
    session.add(parent)
    session.add(child)
    session.commit()
    session.close()


# if __name__ == '__main__':
    # create_user_address()
    # delete_user_address()
    # create_parent_child()
    # parent = session.query(Parent).filter_by(name='John').first()
    # print(parent.name)
    # for child in parent.children:
    #     print(child.name)

    # try:
    #     future_event = Event(
    #         title="New Year Party",
    #         date=datetime.now() + timedelta(days=30),
    #         location="New York")
    #     print(future_event)
    # except ValueError as e:
    #     print(e)

    # user_profile_1 = UserProfile(username='john', password='12345678', email='example@dt.com')
    # print(user_profile_1)
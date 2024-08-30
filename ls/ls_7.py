# from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from services.models import User
from services import engine

Session = sessionmaker(bind=engine)
session = Session()

def create_users_example():
    session.add_all(
        [User(name='Bob', age=22, email='bob@example.com'),
         User(name='David', age=27, email='david@example.com'),
         User(name='Alice', age=30, email='alice@example.com'),
         User(name='Ann', age=17, email='ann2b@example.com'),
         User(name='Ann', age=27, email='ann@example.com')
         ]
    )

    try:
       session.commit()
    except Exception as e:
       session.rollback()
       print('Error:', e)
       print('Rollback done.')


if __name__ == '__main__':
    print('Creating users...')
    create_users_example()
    print('Users created.')
    session.close()
    print('Session closed.')

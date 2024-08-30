from connect2memory import session
from models import Product, Category
from connect2memory import engine
from models import Base

Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    print('Creating engine in memory...')
    try:
        product1 = Product(name='product1', price=100, in_stock=True)
        session.add(product1)
        session.commit()
    except Exception as e:
        print(f'Error: {e}')

    try:
        category1 = Category(name='category1', description='description1')
        session.add(category1)
        session.commit()
    except Exception as e:
        print(f'Error: {e}')

    print('Adding product1 and category1 to session...')
    session.close()
    print('Session closed.')


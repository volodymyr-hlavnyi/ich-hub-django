from sqlalchemy import func

from hw.hw_3.connect2memory import session
from hw.hw_3.models import Product, Category
from hw.hw_3.connect2memory import engine
from hw.hw_3.models import Base

Base.metadata.create_all(bind=engine)


def category_add_new(session):
    try:
        category1 = Category(name="Электроника", description="Гаджеты и устройства.")
        category2 = Category(name="Книги", description="Печатные книги и электронные книги.")
        category3 = Category(name="Одежда", description="Одежда для мужчин и женщин.")
        session.add_all([category1, category2, category3])
        session.commit()
        return category1, category2, category3
    except Exception as e:
        print(f'Error: {e}')
        return None, None, None


def product_add_new(session, category1, category2, category3):
    try:
        product1 = Product(name="Смартфон", price=299.99, in_stock=True, category=category1)
        product2 = Product(name="Ноутбук", price=499.99, in_stock=True, category=category1)
        product3 = Product(name="Научно-фантастический роман", price=15.99, in_stock=True, category=category2)
        product4 = Product(name="Джинсы", price=40.50, in_stock=True, category=category3)
        product5 = Product(name="Футболка", price=20.00, in_stock=True, category=category3)

        session.add_all([product1, product2, product3, product4, product5])
        session.commit()
        return product1, product2, product3, product4, product5
    except Exception as e:
        print(f'Error: {e}')
        return None, None, None, None, None


# Task 2: Read data from the database
def task_2(session):
    categories = session.query(Category).all()
    for category in categories:
        print(f"Категория: {category.name}, Описание: {category.description}")
        for product in category.products:
            print(f"  Продукт: {product.name}, Цена: {product.price}")


def task_3(session):
    # Задача 3: Обновление данных
    smartphone = session.query(Product).filter_by(name="Смартфон").first()
    if smartphone:
        smartphone.price = 349.99
        session.commit()


def task_3_check_update(session):
    updated_smartphone = session.query(Product).filter_by(name="Смартфон").first()
    if updated_smartphone:
        print(f"Обновленная цена смартфона: {updated_smartphone.price}")
    else:
        print("Смартфон не найден.")

def task_4(session):
    # Задача 4: Агрегация и группировка
    product_counts = session.query(Category.name, func.count(Product.id)).join(Product).group_by(Category.id).all()
    for name, count in product_counts:
        print(f"Категория: {name}, Количество продуктов: {count}")

def task_5(session):
    filtered_categories = (
        session.query(
        Category.name, func.count(Product.id))
        .join(Product)
        .group_by(Category.id)
        .having(func.count(Product.id) > 1).all()
    )
    for name, count in filtered_categories:
        print(f"Категория с более чем одним продуктом: {name}, Количество продуктов: {count}")

if __name__ == '__main__':
    print('Creating engine in memory...')

    print("\nTask 1: Add data to the database")

    cat1, cat2, cat3 = category_add_new(session)
    print('\nCategories added.')

    product1, product2, product3, product4, product5 =  product_add_new(session, cat1, cat2, cat3)
    print('Products added.')

    print("Task 2: Read data from the database")
    task_2(session)

    print("\nTask 3: Update data in the database")
    task_3(session)
    task_3_check_update(session)

    print("\nTask 4: Aggregation and grouping")
    task_4(session)

    print("\nTask 5: Filtering grouped data")
    task_5(session)

    session.close()
    print('\nSession closed.')

# use the forkey in sqlite3
# use the python 3.5 as default

# import
import sqlite3

"""
    SQLite3 does not check for foreign key constraints by defautl, you must turn
    this feature on using SQL: PRAGMA Foreign_Keys = ON

"""

def create_product_table(db_name):
    "create the product table"
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("""
                        CREATE TABLE Product(
                            ProductID integer,
                            Name text,
                            Price real,
                            ProductTypeID integer,
                            Primary Key(ProductID),
                            Foreign Key(ProductTypeID) references
                                        ProductType(ProductTypeID))
        """)
        db.commit()


def create_product_type_table(db_name):
    "create the product type table"
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("""
                        CREATE TABLE ProductType(
                            ProductTypeID integer,
                            Description text,
                            Primary Key(ProductTypeID))
        """)
        db.commit()

def query(db_name, sql, data):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA Foreign_Keys = ON")
        cursor.execute(sql, data)
        db.commit()

def insert_into_product(db_name, records):
    "insert data into the product table"
    sql = "INSERT INTO Product(Name, Price, ProductTypeID) VALUES (?,?,?)"
    for record in records:
        query(db_name, sql, record)

def insert_into_product_type(db_name, records):
    "insert data into the product table"
    sql = "INSERT INTO ProductType(Description) VALUES (?)"
    for record in records:
        query(db_name, sql, record)


if __name__ == '__main__':

    db_name = "coffee_shop_1.db"

    try:
        create_product_type_table(db_name)
        create_product_table(db_name)
    except:
        print("table already exists")

    # product_types = [("Cold Drink",), ("Tea",), ("Coffee",)]
    # insert_into_product_type(db_name, product_types)

    # products = [("Moca", 2.4, 3,), ("Green Tea", 1.4, 2,), ("Apple Juice", 4.0, 1,)]
    # products = [("Orange Juice", 3.8, 4,)]
    # insert_into_product(db_name, products)

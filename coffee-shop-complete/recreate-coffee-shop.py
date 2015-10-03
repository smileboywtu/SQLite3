# create the coffee_shop db
# use the python 3.5 and SQLite3 DB

import sqlite3

def query(db_name, sql, data):
    "access the sqlite3 data base"
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute(sql, data)
        db.commit()

def create_customer_table(db_name):
    sql = """
            CREATE TABLE Customer(
                CustomerID  integer,
                FirstName   text,
                LastName    text,
                Street      text,
                Town        text,
                PostCode    text,
                TelephoneNumber text,
                EMailAddress    text,
                Primary Key(CustomerID)
            )
    """
    query(db_name, sql, ())

def create_customer_order_table(db_name):
    sql = """
            CREATE TABLE CustomerOrder(
                OrderID     integer,
                Date        text,
                Time        text,
                CustomerID  integer,
                Primary Key(OrderID),
                Foreign Key(CustomerID) references
                    Customer(CustomerID)
                ON  UPDATE CASCADE ON DELETE CASCADE
            )
    """
    query(db_name, sql, ())

def create_order_item_table(db_name):
    sql = """
            CREATE TABLE OrderItem(
                OrderItemID     integer,
                OrderID         integer,
                ProductID       integer,
                Quantity        integer,
                Primary Key(OrderItemID),
                Foreign Key(OrderID) references
                    CustomerOrder(OrderID)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                Foreign Key(ProductID) references
                    Product(ProductID)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )
    """
    query(db_name, sql, ())

def create_product_table(db_name):
    sql = """
            CREATE TABLE Product(
                ProductID integer,
                Name      text,
                Price     real,
                ProductTypeID integer,
                Primary Key(ProductID),
                Foreign Key(ProductTypeID) references
                    ProductType(ProductTypeID)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )
    """
    query(db_name, sql, ())

def create_product_type_table(db_name):
    sql = """
            CREATE TABLE ProductType(
                ProductTypeID integer,
                Description text,
                Primary Key(ProductTypeID)
            )
    """
    query(db_name, sql, ())

def create_tables(db_name):
    "create the table"
    create_customer_table(db_name)
    create_customer_order_table(db_name)
    create_order_item_table(db_name)
    create_product_table(db_name)
    create_product_type_table(db_name)


def drop_table(db_name, tables):
    "drop the table"
    for table in tables:
        sql = "DROP TABLE IF EXISTS {0}".format(table)
        query(db_name, sql, ())

def main():
    "all table need to be recreated if exists, because table get a foreign key"
    db_name = "coffee_shop.db"

    recreate = False
    response = input("are you sure to erase all the table and create again(y/n)?: ")
    if response.lower() == 'y':
        tables = ("Customer", "CustomerOrder", "OrderItem", "Product", "ProductType")
        drop_table(db_name, tables)
        print("all existing data is erased!")
        recreate = True

    if recreate:
        create_tables(db_name)

if __name__ == '__main__':
    main()

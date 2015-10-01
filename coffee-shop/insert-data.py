# insert data to the db
# use python 3.5 as default


# import
import sqlite3

def insert_data(db_name, table_name, values):
    "insert values in table in db"
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO {0}(Name, Price) VALUES(?,?)".format(table_name), (values))
        db.commit()


if __name__ == '__main__':
    db_name = "coffee_shop.db"
    table_name = "Product"
    value = ("Apple Juice", 10.4)
    insert_data(db_name, table_name, value)

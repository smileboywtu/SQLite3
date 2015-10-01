# search the data in sqlite3
# use the python 3.5 as default

# import
import sqlite3

def select_all_data(db_name, table_name):
    "select all the data from the sqlite"
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM {0}".format(table_name))
        result = cursor.fetchall()

        return result

def select_data(db_name, table_name, id):
    "select data with specific id"
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM {0} WHERE ProductID=?".format(table_name), (id,))
        result = cursor.fetchall()
        return result

def select_specific_data(db_name, table_name, condition):
    "select data with condition"
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM {0} WHERE {1}".format(table_name, condition))
        result = cursor.fetchall()
        return result


if __name__ == '__main__':
    db_name = "coffee_shop.db"
    table_name = "Product"

    result = select_all_data(db_name, table_name)
    print(result)

    result = select_data(db_name, table_name, 1)
    print(result)

    condition = "ProductID > 1"
    result = select_specific_data(db_name, table_name, condition)
    print(result)

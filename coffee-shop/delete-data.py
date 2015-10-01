# update data in the Product table
# use the python 3.5 as default

# import
import sqlite3

def delete_data(db_name, table_name, data):
    "update data in table in db"
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM {0} WHERE ProductID=?".format(table_name), data)
        db.commit()


if __name__ == '__main__':
    db_name = "coffee_shop.db"
    table_name = "Product"
    data = (1, )
    delete_data(db_name, table_name, data)

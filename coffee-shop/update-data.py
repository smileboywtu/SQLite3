# update data in the Product table
# use the python 3.5 as default

# import
import sqlite3

def update_data(db_name, table_name, data):
    "update data in table in db"
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("UPDATE {0} SET Name=?, Price=? WHERE ProductID=?".format(table_name), data)
        db.commit()


if __name__ == '__main__':
    db_name = "coffee_shop.db"
    table_name = "Product"
    data = ("Orange Juice", 8.5, 1, )
    update_data(db_name, table_name, data)

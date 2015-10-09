# manage the product type table
# use the SQLite3 and Python 3.5

# import
import sqlite3

def query(db_name, sql, data):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA Foreign_Keys = ON")
        cursor.execute(sql, data)
        result = cursor.fetchall()
        db.commit()
        return result

def show_all_data(db_name, table_name):
    "show all the data of table from db"
    sql = "SELECT * FROM {0}".format(table_name)
    return query(db_name, sql, ())

def insert_data(db_name, table_name, description):
    "insert new data"
    sql = """
            INSERT INTO {0}(Description)
            VALUES (?)
            """.format(table_name)
    query(db_name, sql,(description,))

def update_data(db_name, table_name, producttypeid, description):
    "update the product"
    sql = """
            UPDATE {0} SET Description=?
            WHERE ProductTypeID=?
            """.format(table_name)
    query(db_name, sql, (description, producttypeid,))

def delete_data(db_name, table_name, producttypeid):
    "delete the product from the table"
    sql = "DELETE FROM {0} WHERE ProductTypeID=?".format(table_name)
    query(db_name, sql, (producttypeid, ))

def print_table(result):
    "show the data in a table"
    print("""

        |{0:^5s}|{1:^15s}|
        """.format("ID",
                   "Description"))
    for entry in result:
        producttypeid, description = entry
        print("""
        {0:^5d} {1:^15s}
            """.format(producttypeid,
                       description))

def ask_question(question, legal):
    "ask the user a question and return the result"
    while 1:
        response = int(input(question))
        if response in legal:
            return response
        print("illegal input, please input data within", legal, "\n")

def print_menu():
    "print the manage menu"
    print("""

        Manage The Product Type Table:

            1. show all product type
            2. insert new data into product type table
            3. update the current product
            4. delete order from repository
            5. return to parent

    """)

def manage_product_type():

    legal = (1, 2, 3, 4, 5)
    question = "\tOperation(1,2,3,4,5): "

    db_name = "coffee_shop.db"
    table_name = "ProductType"

    while 1:
        print_menu()
        response = ask_question(question, legal)

        if response == 1:
            result = show_all_data(db_name, table_name)
            print_table(result)

        elif response == 2:
            print("\tAdd new product type: ")
            description = input("\t\tDescription: ")
            insert_data(db_name,
                        table_name,
                        description)

        elif response == 3:
            result = show_all_data(db_name, table_name)
            print_table(result)
            producttypeid = int(input("\tinput the product type ID: "))
            print("\n\tUpdate the product type information: ")
            description   = input("\t\tDescription: ")
            update_data(db_name,
                        table_name,
                        producttypeid,
                        description)

        elif response == 4:
            result = show_all_data(db_name, table_name)
            print_table(result)
            producttypeid = int(input("\n\tinput the product type id to delete it: "))
            delete_data(db_name, table_name, producttypeid)

        elif response == 5:
            break

        else:
            pass

if __name__ == "__main__":
    manage_order()

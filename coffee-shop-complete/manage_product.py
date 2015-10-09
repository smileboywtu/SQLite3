# manage the product table
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

def insert_data(db_name, table_name, name, price, producttypeid):
    "insert new data"
    sql = """
            INSERT INTO {0}(Name, Price, ProductTypeID)
            VALUES (?,?,?)
            """.format(table_name)
    query(db_name, sql,(name, price, producttypeid))

def update_data(db_name, table_name, productid, name, price, producttypeid):
    "update the product"
    sql = """
            UPDATE {0} SET Name=?, Price=?, ProductTypeID=?
            WHERE ProductID=?
            """.format(table_name)
    query(db_name, sql, (name, price, producttypeid, productid, ))

def delete_data(db_name, table_name, productid):
    "delete the product from the table"
    sql = "DELETE FROM {0} WHERE ProductID=?".format(table_name)
    query(db_name, sql, (productid, ))

def print_table(result):
    "show the data in a table"
    print("""

        |{0:^5s}|{1:^8s}|{2:^9s}|{3:^17s}|
        """.format("ID",
                   "Name",
                   "Price",
                   "ProductTypeID"))
    for entry in result:
        productid, name, price, producttypeid = entry
        print("""
        {0:^5d} {1:^8s} {2:^9s} {3:^17s}
            """.format(productid,
                       name,
                       price,
                       producttypeid))

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

        Manage The Product Table:

            1. show all product
            2. insert new data into product table
            3. update the current product
            4. delete order from repository
            5. return to parent

    """)

def manage_product():

    legal = (1, 2, 3, 4, 5)
    question = "\tOperation(1,2,3,4,5): "

    db_name = "coffee_shop.db"
    table_name = "Product"

    while 1:
        print_menu()
        response = ask_question(question, legal)

        if response == 1:
            result = show_all_data(db_name, table_name)
            print_table(result)

        elif response == 2:
            print("\tAdd new product: ")
            name =  input("\t\tName: ")
            price = input("\t\tPrice: ")
            producttypeid = input("\t\tProductTypeID: ")
            insert_data(db_name,
                        table_name,
                        name,
                        price,
                        producttypeid)

        elif response == 3:
            result = show_all_data(db_name, table_name)
            print_table(result)
            productid = int(input("\tinput the product ID: "))
            print("\n\tUpdate the product information: ")
            name =  input("\t\tName: ")
            price = input("\t\tPrice: ")
            producttypeid = input("\t\tProductTypeID: ")
            update_data(db_name,
                        table_name,
                        productid,
                        name,
                        price,
                        producttypeid)

        elif response == 4:
            result = show_all_data(db_name, table_name)
            print_table(result)
            productid = int(input("\n\tinput the product id to delete it: "))
            delete_data(db_name, table_name, productid)

        elif response == 5:
            break

        else:
            pass

if __name__ == "__main__":
    manage_order()

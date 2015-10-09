# manage the customer order item table
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

def insert_data(db_name, table_name, orderid, productid, quantity):
    "insert new data"
    sql = """
            INSERT INTO {0}(OrderID, ProductID, Quantity)
            VALUES (?,?,?)
            """.format(table_name)
    query(db_name, sql,(orderid, productid, quantity,))

def update_data(db_name, table_name, orderitemid, orderid, productid, quantity):
    "update the product"
    sql = """
            UPDATE {0} SET OrderID=?, ProductID=?, Quantity=?
            WHERE OrderItemID=?
            """.format(table_name)
    query(db_name, sql, (orderid, productid, quantity, orderitemid,))

def delete_data(db_name, table_name, orderitemid):
    "delete the product from the table"
    sql = "DELETE FROM {0} WHERE OrderItemID=?".format(table_name)
    query(db_name, sql, (orderitemid, ))

def print_table(result):
    "show the data in a table"
    print("""

        |{0:^5s}|{1:^11s}|{2:^13s}|{3:^12s}|
        """.format("ID",
                   "OrderID",
                   "ProductID",
                   "Quantity"))
    for entry in result:
        orderitemid, orderid, productid, quantity = entry
        print("""
        {0:^5d} {1:^11s} {2:^13s} {3:^12d}
            """.format(orderitemid,
                       orderid,
                       productid,
                       quantity))

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

        Manage The Customer Table:

            1. show all the order item
            2. insert new data into order item table
            3. update the current order item
            4. delete order from repository
            5. return to parent

    """)

def manage_order_item():

    legal = (1, 2, 3, 4, 5)
    question = "\tOperation(1,2,3,4,5): "

    db_name = "coffee_shop.db"
    table_name = "OrderItem"

    while 1:
        print_menu()
        response = ask_question(question, legal)

        if response == 1:
            result = show_all_data(db_name, table_name)
            print_table(result)

        elif response == 2:
            print("\tAdd new customer order: ")
            orderid =    input("\t\tOrderID: ")
            productid =  input("\t\tProductID: ")
            quantity =   input("\t\tQuantity: ")
            insert_data(db_name,
                        table_name,
                        orderid,
                        productid,
                        quantity)

        elif response == 3:
            result = show_all_data(db_name, table_name)
            print_table(result)

            orderitemid = int(input("\tinput the order item ID: "))
            print("\n\tUpdate the order item information: ")
            orderid =    input("\t\tOrder ID: ")
            productid =  input("\t\tProduct ID: ")
            quantity =   input("\t\tQuantity: ")
            update_data(db_name,
                        table_name,
                        orderitemid,
                        orderid,
                        productid,
                        quantity)

        elif response == 4:
            result = show_all_data(db_name, table_name)
            print_table(result)
            orderitemid = int(input("\n\tinput the order item id to delete it: "))
            delete_data(db_name, table_name, orderitemid)

        elif response == 5:
            break

        else:
            pass

if __name__ == "__main__":
    manage_order()

# manage the customer order table
# use the SQLite3 and Python 3.5

# import
import sqlite3

def show_all_data(db_name, table_name):
    "show all the data of table from db"
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM {0}".format(table_name))
        result = cursor.fetchall()
        return result

def insert_data(db_name, table_name, date, time, customerid):
    "insert new data"
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("""
                    INSERT INTO {0}(Date, Time, CustomerID)
                    VALUES (?,?,?)
                """.format(table_name), (date, time, customerid,))
        db.commit()

def update_data(db_name, table_name, orderid, date, time, customerid):
    "update the product"
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("""
                    UPDATE {0} SET Date=?, Time=?, CustomerID=?
                    WHERE OrderID=?
                """.format(table_name), (date, time, customerid, orderid,))
        db.commit()

def delete_data(db_name, table_name, productid):
    "delete the product from the table"
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM {0} WHERE ProductID=?".format(table_name), (productid, ))
        db.commit()

def print_table(result):
    "show the data in a table"
    print("""

        |{0:^5s}|{1:^14s}|{2:^10s}|{3:^14s}|
        """.format("ID",
                   "Date",
                   "Time",
                   "CustomerID"))
    for entry in result:
        orderid, date, time, customerid = entry
        print("""
        {0:^5d} {1:^14s} {2:^10s} {3:^14d}
            """.format(orderid,
                       date,
                       time,
                       customerid))

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

            1. show all the order
            2. insert new data into order table
            3. update the current order
            4. delete order from repository
            5. return to parent

    """)

def manage_order():

    legal = (1, 2, 3, 4, 5)
    question = "\tOperation(1,2,3,4,5): "

    db_name = "coffee_shop.db"
    table_name = "CustomerOrder"

    while 1:
        print_menu()
        response = ask_question(question, legal)

        if response == 1:
            result = show_all_data(db_name, table_name)
            print_table(result)

        elif response == 2:
            print("\tAdd new customer order: ")
            date =       input("\t\tDate: ")
            time =       input("\t\tTime: ")
            customerid = input("\t\tCustomerID: ")
            insert_data(db_name,
                        table_name,
                        date,
                        time,
                        customerid)

        elif response == 3:
            result = show_all_data(db_name, table_name)
            print_table(result)
            orderid = int(input("input the order ID: "))
            print("\n\tUpdate the order information: ")
            date =       input("\t\tDate: ")
            time =       input("\t\tTime: ")
            customerid = input("\t\tCustomerID: ")
            update_data(db_name,
                        table_name,
                        orderid,
                        date,
                        time,
                        customerid)

        elif response == 4:
            result = show_all_data(db_name, table_name)
            print_table(result)
            orderid = int(input("\ninput the order id to delete it: "))
            delete_data(db_name, table_name, orderid)

        elif response == 5:
            break

        else:
            pass

if __name__ == "__main__":
    manage_order()
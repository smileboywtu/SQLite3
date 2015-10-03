# manage the customer table
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

def insert_data(db_name, table_name, firstname, lastname, street, town, postcode, telephone, email):
    "insert new data"
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("""
                    INSERT INTO {0}(FirstName, LastName, Street, Town, PostCode, TelephoneNumber, EMailAddress)
                    VALUES (?,?,?,?,?,?,?)
                """.format(table_name), (firstname, lastname, street, town, postcode, telephone, email,))
        db.commit()

def update_data(db_name, table_name, customerid, firstname, lastname, street, town, postcode, telephone, email):
    "update the product"
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("""
                    UPDATE {0} SET FirstName=?, LastName=?, Street=?, Town=?, PostCode=?, TelephoneNumber=?, EMailAddress=?
                    WHERE CustomerID=?
                """.format(table_name), (firstname, lastname, street, town, postcode, telephone, email, customerid,))
        db.commit()

def delete_data(db_name, table_name, customerid):
    "delete the product from the table"
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM {0} WHERE CustomerID=?".format(table_name), (customerid, ))
        db.commit()

def print_table(result):
    "show the data in a table"
    print("""

        |{0:^5s}|{1:^13s}|{2:^10s}|{3:^10s}|{4:^10s}|{5:^12s}|{6:^20s}|{7:^20s}|
        """.format("ID",
                   "FirstName",
                   "LastName",
                   "Street",
                   "Town",
                   "PostCode",
                   "TelephoneNumber",
                   "EMailAddress"))
    for entry in result:
        customerid, firstname, lastname, street, town, postcode, telephone, email = entry
        print("""
        {0:^5d} {1:^13s} {2:^10s} {3:^10s} {4:^10s} {5:^12s} {6:^20s} {7:^20s}
            """.format(customerid,
                       firstname,
                       lastname,
                       street,
                       town,
                       postcode,
                       telephone,
                       email))

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

            1. show all the customer
            2. insert new data into customer
            3. update the current customer
            4. delete product from repository
            5. return to parent

    """)

def manage_customer():

    legal = (1, 2, 3, 4, 5)
    question = "\tOperation(1,2,3,4,5): "

    db_name = "coffee_shop.db"
    table_name = "Customer"

    while 1:
        print_menu()
        response = ask_question(question, legal)

        if response == 1:
            result = show_all_data(db_name, table_name)
            print_table(result)

        elif response == 2:
            print("\tAdd new customer: ")
            firstname = input("\t\tFirst Name: ")
            lastname =  input("\t\tLast  Name: ")
            street =    input("\t\tStreet: ")
            town =      input("\t\tTown: ")
            postcode =  input("\t\tPost Code: ")
            telephone = input("\t\tTelephone: ")
            email =     input("\t\tEmail: ")
            insert_data(db_name,
                        table_name,
                        firstname,
                        lastname,
                        street,
                        town,
                        postcode,
                        telephone,
                        email)

        elif response == 3:
            result = show_all_data(db_name, table_name)
            print_table(result)
            customer = int(input("input the customer ID: "))
            print("\n\tUpdate the customer information: ")
            firstname = input("\t\tFirst Name: ")
            lastname =  input("\t\tLast  Name: ")
            street =    input("\t\tStreet: ")
            town =      input("\t\tTown: ")
            postcode =  input("\t\tPost Code: ")
            telephone = input("\t\tTelephone: ")
            email =     input("\t\tEmail: ")
            update_data(db_name,
                        table_name,
                        firstname,
                        lastname,
                        street,
                        town,
                        postcode,
                        telephone,
                        email)

        elif response == 4:
            result = show_all_data(db_name, table_name)
            print_table(result)
            productid = int(input("\ninput the customer id to delete it: "))
            delete_data(db_name, table_name, productid)

        elif response == 5:
            break

        else:
            pass

if __name__ == "__main__":
    manage_customer()

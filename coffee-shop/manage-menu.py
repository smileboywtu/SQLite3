# this is a short program to manage the product DB
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

def insert_data(db_name, table_name, name, price):
    "insert new data"
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO {0}(Name, Price) VALUES (?,?)".format(table_name), (name, price,))
        db.commit()

def update_data(db_name, table_name, productid, name, price):
    "update the product"
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("UPDATE {0} SET Name=?, Price=? WHERE ProductID=?".format(table_name), (name, price, productid,))
        db.commit()

def delete_data(db_name, table_name, productid):
    "delete the product from the table"
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM {0} WHERE ProductID=?".format(table_name), (productid, ))
        db.commit()

def print_table(result):
    "show the data in a table"
    print("{0:<10s}      {1:<20s}     {2:<6s}".format("ProductID", "Name", "Price"))
    for entry in result:
        productid, name, price = entry
        print("{0:^10d}     {1:<20s}     {2:>6.2f}".format(productid, name, price))

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

            1. show all the products
            2. insert new data into products
            3. update the current product
            4. delete product from repository
            5. exit

    """)

def main():
    "main test function"

    legal = [1, 2, 3, 4, 5]
    question = "Operation: "

    db_name = "coffee_shop.db"
    table_name = "Product"

    while 1:
        print_menu()
        response = ask_question(question, legal)

        if response == 1:
            result = show_all_data(db_name, table_name)
            print_table(result)

        elif response == 2:
            name = input("please input the new product name: ")
            price = float(input("please input the price of the new product: "))
            insert_data(db_name, table_name, name, price)

        elif response == 3:
            result = show_all_data(db_name, table_name)
            print_table(result)
            productid = int(input("please input the product ID which to update: "))
            name = input("input new product name: ")
            price = float(input("input the new price: "))
            update_data(db_name, table_name, productid, name, price)

        elif response == 4:
            result = show_all_data(db_name, table_name)
            print_table(result)
            productid = int(input("please input the product id to delete it: "))
            delete_data(db_name, table_name, productid)

        elif response == 5:
            break

        else:
            pass

    input("\n\nThanks for using this system, welcome back.\n")

if __name__ == "__main__":
    main()

# manage the coffee Shop
# use the python 3.5 as default

from manage_customer import manage_customer
from manage_order import manage_order
from manage_order_item import manage_order_item

def print_menu():
    print("""

            Welcome To Coffee Shop

        1)  manage customer
        2)  manage order
        3)  manage order item
        4)  manage product
        5)  manage product type
        6)  exit

    """)

def ask_question(question, legal):
    "ask the user a question and return the result"
    while 1:
        response = int(input(question))
        if response in legal:
            return response
        print("illegal input, please input data within", legal, "\n")

def main():

    legal = (1, 2, 3, 4, 5, 6)
    question = "\tOperation(1,2,3,4,5,6): "

    while 1:
        print_menu()
        response = ask_question(question, legal)

        if response == 1:
            manage_customer()
        elif response == 2:
            manage_order()
        elif response == 3:
            manage_order_item()
        elif response == 4:
            manage_product()
        elif response == 5:
            manage_product_type()
        elif response == 6:
            break
        else:
            pass

    input("\n\nThanks for using this system, welcome back.\n")

if __name__ == '__main__':
    main()

# Introduction

this demon create the complete coffee shop database which can be used to manage the products and customers of the coffee shop.

# Entitis Design

 - ## ER Diagram
<<<<<<< HEAD
    ![Alt Text](http://www.pythonschool.net/databases/images/coffee_shop_er_diagram.png "ER Diagram of coffee shop from python school")
=======
![Alt Text](http://www.pythonschool.net/databases/images/coffee_shop_er_diagram.png "ER Diagram of coffee shop from python school")
>>>>>>> 7fd9a1d51ed25839f41c82a12590230dc073f8db

 - ## Entity Description
    + Customer(**CustomerID**, FirstName, LastName, Street, Town, PostCode, TelephoneNumber, EMailAddress)

    + CustomerOrder(**OrderID**, Date, Time, *CustomerID*)

    + OrderItem(**OrderItemID**, *OrderID*, *ProductID*, Quantity)

    + Product(**ProductID**, Name, Price, *ProductTypeID*)

    + ProductType(**ProductTypeID**, Description)

# Management App Design

![Alt Text](http://www.pythonschool.net/databases/images/coffeeshopclassdiagram.png "design the manage app, this comes from the python school")

# Tips

All the diagram and design are from python school, please keep care of this.

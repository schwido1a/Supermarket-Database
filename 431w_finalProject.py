import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123456',
    port = '3306',
    database = '431w_finalproject'
)

mycursor = mydb.cursor()


def userManuel():
    print("Welcome to GroceryStore.app, which table would you like to access:")
    print("1. Items\n"
          "2. Discount\n"
          "3. Employee\n"
          "4. Feedback\n"
          "5. Members\n"
          "6. Membership\n"
          "7. Supplier\n"
          "8. Transactions\n"
          "9. Quit")
    choice = input("Enter your choice (1-9): ")
    return choice

def main():
    while True:
        choice = userManuel()
        if choice == '1':
            print("What do you want to do with the table:")
            print("1. Add a record\n"
                  "2. Delete a record\n"
                  "3. Update a existing record\n"
                  "4. Find a record\n"
                  "5. Retrive to main menu\n"
                  "6. Other command")
            choice = input("Enter your choice (1-5): ")
            if choice == '5':
                continue
            elif choice == '1': # add a record
                print("Enter details for the new item:")
                itemID = input("Item ID is: ")
                itemName = input("Item  is: ")
                category = input("Category is(optional): ")
                price = input("Price is: ")
                stockStatus = input("in-stock or out-of-stock: ")
                quantity = input("Quantity is(optional): ")
                if not category:
                    category = None
                if not quantity:
                    quantity = 0
                sqlCommand1 = "INSERT INTO Items (itemID, itemName, category, price, stockStatus, quantity) VALUES (%s, %s, %s, %s, %s, %s)"
                commandValue = (itemID, itemName, category, price, stockStatus, quantity)
                try:
                    mycursor.execute(sqlCommand1, commandValue)
                    print("Record Added!")
                except mysql.connector.Error as error:
                    print("Error: ", error)
            elif choice == '2': #delete a record
                itemID = input("Item ID is: ")
                sqlCommand2 = "delete from Items where itemID = " + itemID
                try:
                    mycursor.execute(sqlCommand2)
                    mydb.commit()
                    if mycursor.rowcount > 0:
                        print("Record deleted!")
                    else:
                        print("No record found")
                except mysql.connector.Error as error:
                    print(f"Error: ", error)
            elif choice == '3': #update an existing record
                print("Enter the Item ID for updating:")
                itemID = input("Item ID is: ")
                print("Which field do you want to update?")
                print("1. Item Name\n"
                      "2. Category\n"
                      "3. Price\n"
                      "4. Stock Status\n"
                      "5. Quantity")
                choice3 = input("Enter your choice (1-5): ")
                if choice3 == '1':
                    new_value = input("Enter the Name: ")
                    sqlCommand3 = "UPDATE Items SET itemName = %s WHERE itemID = %s"
                elif choice3 == '2':
                    new_value = input("Enter the Category: ")
                    sqlCommand3 = "UPDATE Items SET category = %s WHERE itemID = %s"
                elif choice3 == '3':
                    new_value = input("Enter the Price: ")
                    sqlCommand3 = "UPDATE Items SET price = %s WHERE itemID = %s"
                elif choice3 == '4':
                    new_value = input("in-stock/out-of-stock: ")
                    sqlCommand3 = "UPDATE Items SET stockStatus = %s WHERE itemID = %s"
                elif choice3 == '5':
                    new_value = input("Enter the Quantity: ")
                    sqlCommand3 = "UPDATE Items SET quantity = %s WHERE itemID = %s"
                else:
                    print("wrong input, returning to menu")
                    continue
                commandValue3 = (new_value, itemID)
                try:
                    mycursor.execute(sqlCommand3, commandValue3)
                    if result:
                        print("Record updated!")
                    else:
                        print("No record found")
                except mysql.connector.Error as error:
                    print(f"Error: ", error)
            elif choice == '4': #look up a record with ID
                print("Enter the Item ID to look up:")
                itemID = input("Item ID: ")
                sqlCommand4 = "select * from Items where itemID = " + itemID
                try:
                    mycursor.execute(sqlCommand4)
                    result = mycursor.fetchone()
                    if result:
                        print("Record found:", result)
                    else:
                        print("No record found with that ID.")
                except mysql.connector.Error as error:
                    print("Error: ", error)
                    print("Returning to main menu")
            elif choice == '6':
                print("Enter the command:")
                sqlCommand6 = ""
                try:
                    mycursor.execute(sqlCommand6)
                    result = mycursor.fetchone()
                    if result:
                        print(result)
                    else:
                        print("Nothin happend")
                except mysql.connector.Error as error:
                    print("Error: ", error)
                    print("Returning to main menu")
        elif choice == '2':
            print("Welcome to Discount table! You are only allowed to sort by discount value here!")
            choice1 = input("Enter 1 if you would like to sort by discountValue, enter others to retrive to main menu: ")
            if choice1 == '1':
                sqlCommand1 = "select * from Discount order by discountValue DESC"
                try:
                    mycursor.execute(sqlCommand1)
                    results = mycursor.fetchall()
                    if results:
                        print("sorted!")
                        for result in results:
                            print(result)
                    else:
                        print("Something weird happened")
                except mysql.connector.Error as error:
                    print("Error: ", error)
                    print("Returning to main menu")
            else:
                continue
        elif choice == '3':
            print("Function is currently unavaliable, please come back later!")
        elif choice == '4':
            print("This table is still under construction")
        elif choice == '5':
            print("This database is not ready ye")
        elif choice == '6':
            print("It's 7pm and we are closed")
        elif choice == '7':
            print("I will get back to you later")
        elif choice == '8':
            print("Last one, hang in there!")
        elif choice == '9':
            print("Thank you for using this app, hope we get full marks on everything!")
            break

        else:
            print("Wrong number, only input number from 1-9!")
    mycursor.close()
    mydb.close()

if __name__ == "__main__":
    main()



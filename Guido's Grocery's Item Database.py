def display_menu():

    print("Enter 1 to display the table of our products")
    print("Enter 2 to add a product")   
    print("Enter 3 to caclulate the average cost of the items")
    print("Enter 4 to caclulate the total number of individual items")
    print("Enter 0 to exit the program")


def user_choice():

    good_input= False
    while (not good_input):
        user_input= input("what would you like to do? ")
        try:
            choice= int(user_input)
            if (choice < 0 or choice > 4):
                raise ValueError
            return choice
        except ValueError:
            print("input not an integer")

def display_table(grocery_data):
    print("Product Name".ljust(16), "UPC".ljust(16), "Price".ljust(16), "Number in Stock".ljust(15), sep="")
    for product in grocery_data:
        print (product[0].ljust(15),str(product[1]).ljust(15), str(product[2]).ljust(15), str(product[3]).ljust(15))




def main():

    grocery_data= [
        ["Milk",95520, 3.27, 20 ], ["Eggs",55504, 2.97, 15], ["Bread", 57971, 2.78 , 20], ["Apples", 19791, 0.78, 70],["Cheese Bits", 32510, 2.99, 25], ["Cheese Bytes", 84159, 23.92, 10]] 

    print("Welcome to Guido's Grocery's Item Database")
    choice=-1
    while (choice  != 0 ):
        display_menu()
        choice = user_choice()
        if (choice == 1 ):
            display_table(grocery_data)
                        
            
        if (choice == 2 ):
            add_product(grocery_data)
            
        if (choice == 3 ):
            avg_price(grocery_data)
        if (choice == 4 ):
            total_stock(grocery_data)
      



    





def add_product(grocery_data):
    product= []
    product.append(input("Please enter the product name: "))
    product.append(int(input("Please enter the UPC: ")))
    product.append(float(input("Please enter the price: ")))
    product.append(int(input("Please enter the number in stock: ")))
    grocery_data.append(product)
    print( product[0], "added!")



def avg_price(grocery_data):
    total = 0
    for product in grocery_data:
        total += product[2]
    average = total/len(grocery_data)
    
    

    print("The average cost of the items in stock is " + str(average))

def total_stock(grocery_data):
    total = 0
    for product in grocery_data:
        total += product[3]
    print("The total number of items currently in stock is " + str(total) )









main()

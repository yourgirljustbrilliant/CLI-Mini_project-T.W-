from colorama import Fore, Back, Style

def products_menu():
    print("\t0) Quit")
    print("\t1) Display product list")
    print("\t2) Create a new product")
    print("\t3) Update an existing product")
    print("\t4) Delete a product")
product_lists = []
#product_lists =["Sandwich","Soup","Salads","Pasta","Chicken",]

def update_product():
    print("\tYou can now update an existing product from their index value below\n")
    products =["Salds","furits_bowl","sandwiches","green_juice","water",
    "pasta_dish","sweet_potato_chips","wings"]
    for count, product in enumerate(products,start=1):
        print(f"[{count}] {product}")
    choice = int(input("\t\nEnter a product index \n"))
    products [choice] = input("update product name:\n")
    print(product_lists)
    if choice < 0 or choice >= len(products) :
        print("choice not found")
    else:
        print(f"You have updated a product name to {products [choice]}")


def delete_product():
    print("\tYou are about to delete a product from the product list\n")
    products =["Salds","Furits_Bowl","Sandwiches","Green_Juice","Water",
    "Pasta_Dish","Sweet_Potato_Chips","Wings"]
    print(products)
    del_item = input(Back.BLACK +Fore.LIGHTBLUE_EX + "\t\nEnter the product you want to delete:\n").title()
    if del_item in products:
        print(Style.RESET_ALL)
        products.remove(del_item)
        print()
        print(f" You have now deleted a product,\n here is the new list of products:\n{products}")
    else:
        print()
        print("\tItem not found in the list\n")
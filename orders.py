from product import product_lists
from colorama import Fore, Back, Style
import csv
from tqdm import tqdm
import time


def order_menu():
      print("1) Display orders list")
      print("2) Create a order")
      print("3) Update existing order status")
      print("4) Update existing order")
      print("5) Delete order")
      print("0) Return to main menu")

new_order = {"customer_name":"",
"customer_address":"",
"customer_phone": "",
"courier":"" 
"status" "",
"items":""}

order_list =[]

order_status =["Preparing","Ready for dispatch","Dispatch","Delivered"]

courier_list = []

def orders():
    products =["Salds","Furits_Bowl","Sandwiches","Green_Juice","Water",
    "Pasta_Dish","Sweet_Potato_Chips","Wings"]
    print("\tEnter the products you want to order from our products list,\n"+
     "\tusing its index number speparated by a comma,\n")
    for count, product in enumerate(products,):
        print(f"[{count}] {product}")
    print()
    user_order =(input("Enter your selection now\n")).split(',')
    converted_order = "{}".format(user_order)
    print()
    print(f"You choose\n"+ converted_order)


def create_order():
        order_status =["Preparing","Ready for dispatch","Dispatch","Delivered"]
        print(Fore.WHITE + Style.BRIGHT +"\tCreate your order below\n")
        name_value = input("\tEnter customer name\n")
        address_value = input("\t Enter your address\n")
        phone_value = input("\t Enter your phone number \n")
        order_status = "preparing"
        new_order ["customer_name"] = name_value 
        new_order ["customer_address"] = address_value
        new_order ["customer_phone"] = phone_value
        new_order ["status"] = order_status
        print()

        products =["Salds","Furits_Bowl","Sandwiches","Green_Juice","Water",
    "Pasta_Dish","Sweet_Potato_Chips","Wings"]
        print(Fore.WHITE +"\tEnter the products you want to order from our products list,\n"+
     "\tusing its index number speparated by a comma,\n")

        for count, product in enumerate(products,start=1):
             print(f"[{count}] {product}")
        print()

        user_order =(input("\tEnter your selection now\n")).split(',')
        converted_order = "{}".format(user_order)
        print()
        new_order ["items"] = converted_order
        print("\t Now choose your courier from our list of couriers below\n")
        print()
        with open("courier.csv","r") as courier_csv:
            reader = csv.DictReader(courier_csv)
            for lines in reader:
                courier_list.append(lines)
    
        for index, value in enumerate(courier_list,start=1):
            print( index,value)
        print()
        courier_index = int(input("\t Select a courier by their index\n"))
        print()
        new_order ["courier"] = courier_index
        #add progress bar...put label that says >>>print("\tYour order is being prepard\n")<<<
        print("\tThis is your order\n")    
        
        display_dict = '\n'.join(f'{key}: {value}' for key, value in new_order.items())
        order_list.append(new_order)
        print(order_list)
        print()
        print("---------------------------------------------------------------------------------------")
        print(Fore.BLUE +Style.BRIGHT+"\t Please check that all your information provided is correct!\n" + 
        "\tIf you need to make changes please seclect update order in order menu!\n" +
        "\t Otherwise please continue!\n")
        print("---------------------------------------------------------------------------------------")


def update_existing_order_status():
    print(Fore.WHITE+ "*")
    for index,value in enumerate(order_status,start=1):
        print(index,value)
    print()
    order_status_index = int(input(Fore.WHITE+"\tSelect a new status from the status index value\n"))
    new_order ["status"] = order_status_index
    order_list.append(new_order)
    print()
    print(f"\tThis is your updated order\n{new_order}\n")


def update_existing_order():  
    for key,value in new_order.items():
        user_input = input(f"{key}")
        if user_input !="":
            new_order[key] = user_input

    if user_input=="":
        print()
        print(Fore.BLUE+"\tno property was updated!\n")
        print()
    
    else:
        print(Fore.GREEN+"<<<<<<<<  Implementing your update  >>>>>>>>\n")
        for i in tqdm([1,2,3,4,5]):
           time.sleep(0.3)
        print(new_order)
    

# dispatched(50%) delivered(100%)

def delete_order():
    print(Fore.CYAN+"\tYou are about to delete a item from order\n")
    for index, value in enumerate(new_order.items(),start=1):
          print(f"{index} {value}")
    delete_order = int(input("\tEnter the order you want to delete using its index\n"))
    if delete_order == 1:
        del new_order["customer_name"]
    elif delete_order == 2:
        del new_order["customer_address"]
    elif delete_order == 3:
        del new_order["customer_phone"]
    elif delete_order == 4:
        del new_order["courier"]
    elif delete_order == 5:
        del new_order["status"]
    elif delete_order == 6:
        del new_order["items"]
    print(f"Your new order list looks like this: {new_order}")

  
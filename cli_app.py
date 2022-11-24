from colorama import Fore, Back, Style
import csv
from csv import writer,DictWriter
import os
import pathlib
from time import sleep
from tqdm import tqdm
from couriers import courier_menu, create_new_courier, courier_list, delete_courier, update_existing_courier
from menu import main_menu
from orders import create_order, delete_order, order_menu,order_list,new_order, orders, update_existing_order, update_existing_order_status
from product import delete_product, products_menu,product_lists, update_product



def saving_all_data():
    product_fieldnames = ["product_names","product_price"]
    with open("product.csv","a") as save_products:
        product_fieldnames = ["product_names","product_price"]
        writer = csv.DictWriter(save_products, fieldnames=product_fieldnames)
        writer.writeheader()
        writer.writerows(product_lists)

    
    with open("orders.csv","a") as save_order:
        reader = csv.DictWriter(save_order,fieldnames=order_list)
        reader.writeheader()
        reader.writerow(new_order)# get help for saving
        
    with open("courier.csv","w") as save_courier:
        courier_fieldnames = ["name_of_courier,couriers_phone_number"]
        writer= csv.DictWriter(save_courier, fieldnames=courier_fieldnames)
        writer.writeheader()
        writer.writerows(courier_list)




while True:
    main_menu()
    option =input("\tChoose your option from our menu:\n")

    if option == "0":
        print("<<<<<<<<<<<  SAVING ALL DATA  >>>>>>>>>>>>>>>\n")
        saving_all_data()
        print(Fore.RED +"<<<<<<<<<<<<<  EXITTING APP  >>>>>>>>>>>>>>>>\n")
        break

    elif option == "1":
        while True :
            print(Fore.LIGHTGREEN_EX +"\tProducts menu")
            products_menu()
            option =input("\tChoose your option from our menu:\n")
                            
            if option == "0":
                print(Fore.LIGHTYELLOW_EX +"Returning to Main menu")
                break
            elif option == "1":
                print(Fore.BLACK + "\tDisplaying product list")
                print()
                
                with open("products.csv", "r") as csv_file:
                   csv_reader = csv.DictReader(csv_file)
                   for lines in csv_reader:
                     product_lists.append(lines)
                print(product_lists)
                print(Style.RESET_ALL)

            elif option =="2":
                print(Fore.WHITE +"\tCreate a new product\n")
                print(Style.RESET_ALL)
                suggestion =input(Back.BLACK +Fore.LIGHTBLUE_EX +"Enter your Suggestion\n")
                print()
                product_lists.append(suggestion)
                print()
                print(Style.RESET_ALL)
                print(product_lists)
                print()
            elif option == "3":
                update_product()
                print(Style.RESET_ALL)
            elif option == "4": 
                delete_product()
                print()
        
            
    elif option =="2":
        while True:
            print(Fore.RED +"\tOrders menu")
            order_menu()
            option =input("\tChoose your option from our menu:\n")

            if option == "0":
                        print(Fore.LIGHTYELLOW_EX +"Returning to Main menu")
                        break

            if  option == "1":
                print(Fore.WHITE+"\tYou are now viewing orders dictionary\n")
                print()
                with open('orders.csv','r') as orders_csv:
                    reader = csv.DictReader(orders_csv)
                    for order in reader:
                        order_list.append(order)
                    print(order_list)
                 
            elif option == "2":
                print()
                create_order()
             
            elif option == "3":
                update_existing_order_status()
                
            elif option == "4":
                print(Fore.WHITE + Style.BRIGHT+"\tUpdate existing order\n")
                update_existing_order()
            elif option == "5":
                delete_order()
                
                    
    elif option == "3":
        while True:
            print(Fore.LIGHTMAGENTA_EX + "\tCouriers menu\n")
            courier_menu()
            option =input("\tChoose your option from our menu:\n")

            if option =="0":
                print(Fore.LIGHTYELLOW_EX +"\t Returning to main menu\n")
                break

            elif option =="1":
                print("\t This is our list of couriers\n")
                with open("courier.csv","r") as courier:
                    reader = csv.DictReader(courier)
                    for couriers in reader:
                      print(courier.readlines())
                #courier_list.append(courier)
                

            elif option =="2":
                print("\t You are about to create a new courier\n")
                create_new_courier()
            elif option =="3":
                print("\tYou can now update an existing courier\n")
                update_existing_courier()
                
            elif option =="4":
                print("\t Choose the courier you want to delete\n")
                delete_courier()
                

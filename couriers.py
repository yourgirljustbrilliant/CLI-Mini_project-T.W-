from colorama import Fore, Back, Style
import csv

new_courier_name = 0
new_courier_number = 0

def courier_menu():
      print("1) Display couriers list")
      print("2) Create new courier")
      print("3) Update existing courier")
      print("4) Delete courier")
      print("0) Return to Main menu")

courier_list = ["jen","roger","lute","rose"]

def create_new_courier():
        globalnew_courier_name = input("\t Enter couriers name\n")
        globalnew_courier_number = input("\tEnter couriers phone number\n")
        print()
        print("\tYour courier was added,see list below\n")
        courier_list.append({"name_of_courier":globalnew_courier_name,"courier_phone_number":globalnew_courier_number})
        print()
        print(courier_list)
        print()
        
def update_existing_courier():
    for count, courier in enumerate(courier_list,start=1):
        print(f"{count},{courier}")
        print()
        courier_update =int(input("\tEnter the courier you would like to update by their index\n"))
        print(courier_list[courier_update])
    

def delete_courier():
    for index,value in enumerate(courier_list):
        print()
        print(index,value)
        del_courier = int(input("\t Enter the courier you want to delete by their index\n"))
        del courier_list[del_courier]
        print(courier_list)
#create a progress bar to show status being prepared(15%)ready for dispatch(25%) 

order_status =["Preparing","Ready for dispatch","Dispatch","Delivered"]


def print_couriers():# meant to be in orders section 
    '''for each courier GET user input for courier index SET order status to be 'PREPARING'''
    with open("courier.csv","r") as files:
        for count , courier in enumerate(courier_list,start=1):
            print(f"[{count}] {courier}")
            print()
            your_courier = int(input("\tChoose your courier from our list\n"))
            order_status = "Preparing"
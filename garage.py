import json
import os
from helper_garage import menu

Garage = []
MY_DATA = 'garage.txt'

   
def load_data():
    global Garage
    with open(MY_DATA, 'r') as filehandle:
        Garage = json.load(filehandle) 

def save_2_file():
    with open(MY_DATA, 'w') as filehandle:
        json.dump(Garage, filehandle)


def do_menu_actions(userSelection):
    if userSelection == 'x': # when closing the applicaion
        save_2_file()
        print("bye bye")
        exit()
    elif userSelection == 'p': print(Garage)
    elif userSelection == 'a': Garage.append({"color":input("which color?"),"model":input("which model?"),"brand":input("which brand?")})
    elif userSelection == 'e':   
 
        print("Edit existing car:")
        print(Garage)  # רשימת המכוניות בג'ראג'

        car_index = int(input("Enter the index of the car you want to edit: "))
        if 0 <= car_index < len(Garage):
        # מדפיס את פרטי המכונית הנוכחית
            print(f"Current details: {Garage[car_index]}")

        # שינוי פרטי המכונית
            Garage[car_index]["color"] = input("Enter new color: ")
            Garage[car_index]["model"] = input("Enter new model: ")
            Garage[car_index]["brand"] = input("Enter new brand: ")

            print(f"Car at index {car_index} has been updated.")
            print(Garage)  # רשימת המכוניות לאחר העדכון
        else:
            print("Invalid index. No car has been edited.")
    elif userSelection == 'd': 
     

        print("Delete existing car:")
        print(Garage)  # רשימת המכוניות בג'ראג'

        car_index = int(input("Enter the index of the car you want to delete: "))
        if 0 <= car_index < len(Garage):
        # מדפיס את פרטי המכונית הנמחקת
            print(f"Deleting car: {Garage[car_index]}")

        # מחיקת המכונית מרשימת המכוניות
            deleted_car = Garage.pop(car_index)

            print(f"Car at index {car_index} has been deleted: {deleted_car}")
            print(Garage)  # רשימת המכוניות לאחר המחיקה
        else:
            print("Invalid index. No car has been deleted.")

def main():
    load_data() 
    while True:
        menu()
        userSelection = input("please select action")
        os.system('cls' if os.name == 'nt' else 'clear') #clear terminal
        do_menu_actions(userSelection)
        

if __name__ == "__main__":
    main()
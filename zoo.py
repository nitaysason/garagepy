import json
import os


zoo = []
MY_DATA = 'zoo.txt'

   
def load_data():
    global zoo
    with open(MY_DATA, 'r') as filehandle:
        zoo = json.load(filehandle) 

def save_2_file():
    with open(MY_DATA, 'w') as filehandle:
        json.dump(zoo, filehandle)


def do_menu_actions(userSelection):
    if userSelection == 'x': # when closing the applicaion
        save_2_file()
        print("bye bye")
        exit()
    elif userSelection == 'p': print(zoo)
    elif userSelection == 'a': zoo.append({"color":input("which color?"),"age":input("which age?"),"animal":input("which animal?")})
    elif userSelection == 'e':   
 
        print("Edit existing animal:")
        print(zoo)  # רשימת המכוניות בג'ראג'

        anim_index = int(input("Enter the index of the animal you want to edit: "))
        if 0 <= anim_index < len(zoo):
        # מדפיס את פרטי המכונית הנוכחית
            print(f"Current details: {zoo[anim_index]}")

        # שינוי פרטי המכונית
            zoo[anim_index]["color"] = input("Enter new color: ")
            zoo[anim_index]["age"] = input("Enter new age: ")
            zoo[anim_index]["animal"] = input("Enter new animal: ")

            print(f"Car at index {anim_index} has been updated.")
            print(zoo)  # רשימת המכוניות לאחר העדכון
        else:
            print("Invalid index. No animal has been edited.")
    elif userSelection == 'd': 
     

        print("Delete existing animal:")
        print(zoo)  # רשימת המכוניות בג'ראג'

        anim_index = int(input("Enter the index of the animal you want to delete: "))
        if 0 <= anim_index < len(zoo):
        # מדפיס את פרטי המכונית שימומשת
            print(f"Deleting animal: {zoo[anim_index]}")

        # מחיקת המכונית מרשימת המכוניות
            deleted_animal = zoo.pop(anim_index)

            print(f"animal at index {anim_index} has been deleted: {deleted_animal}")
            print(zoo)  # רשימת המכוניות לאחר המחיקה
        else:
            print("Invalid index. No animal has been deleted.")


    

def menu():
    print("p - print all animals")
    print("x - exit")
    print("d - delete")
    print("a - add a animal")
    print("e - edit the animal")


def main():
    load_data() 
    while True:
        menu()
        userSelection = input("please select action")
        os.system('cls' if os.name == 'nt' else 'clear') #clear terminal
        do_menu_actions(userSelection)
        

if __name__ == "__main__":
    main()
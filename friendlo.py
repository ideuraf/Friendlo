import json
import os
import sys

file_path = r"C:\friendlo\data.json"

def load_names():
    try:
        if not os.path.exists(file_path):
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w") as file:
                json.dump({}, file)
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"error creating file: {e}")
        return {}

def retrieveInfo(person, names):
    if person in names:
        if not names[person]:
            print(f"\nNo Information On {person}")
        else:
            print(f"\n\033[94mInformation For\033[0m \033[92m{person}\033[0m:")
            for info_type, info in names[person].items():
                print(f"\033[91m{info_type}\033[0m: \033[95m{info}\033[0m")
    else:
        print("Person Not Found")

def getPeople(names):
    if not names:
        print("No Names Stored")
        return
        
    name_list = list(names.keys())
    for index, name in enumerate(name_list, start=1):
        print(f"\033[95m[{index}]\033[0m \033[93m{name}\033[0m")
    
    try:
        choice = int(input("Selection: "))
        if 1 <= choice <= len(name_list):
            retrieveInfo(name_list[choice-1], names)
        else:
            print("Invalid Selection")
    except ValueError:
        print("Please Enter A Valid Number")

def add_info_to_person(names, person):
    info_type = input("Type of Info: ")
    info_value = input(f"Enter the {info_type}: ")
    
    names[person][info_type] = info_value
    with open(file_path, "w") as file:
        json.dump(names, file, indent=4)
    print("Information Added Successfully")

def add_name(names):
    print("\n[1] Add New Person\n[2] Add Info to Existing Person")
    choice = input("Selection: ")
    
    if choice == "1":
        name = input("Name: ")
        if name in names:
            print("Name Already Exists")
        else:
            names[name] = {}
            with open(file_path, "w") as file:
                json.dump(names, file, indent=4)
            print("Person Added Successfully")
    
    elif choice == "2":
        if not names:
            print("No Existing People. Please Add A Person First")
            return
            
        print("\nExisting People:")
        name_list = list(names.keys())
        for index, name in enumerate(name_list, start=1):
            print(f"[{index}] {name}")
            
        try:
            selection = int(input("Select A Person: "))
            if 1 <= selection <= len(name_list):
                selected_person = name_list[selection-1]
                add_info_to_person(names, selected_person)
            else:
                print("Invalid Selection")
        except ValueError:
            print("Please Enter A Valid Number")
    
    else:
        print("Invalid Choice")

print("\033[93mどうも, for friendlo, 仕方ない!!\033[0m")
names = load_names()

def mainInput():
    while True:
        action = input(f"\n\033[92m[1] Receive\033[0m \033[94m[2] Admit\033[0m \033[91m[3] Exit\033[0m\n")

        if action == "1":
            getPeople(names)
        elif action == "2":
            add_name(names)
        elif action == "3":
            sys.exit()
        else:
            print("Invalid Choice")

mainInput()
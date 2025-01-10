import random

print("Welcome to using a password generator.")

def prompt():
    global length
    try:
        length = int(input("How long should the password be: "))
    except ValueError:
        print("Please input an integer")
        prompt()

def generator():
    global pwd
    pwd = random.randint(0, int("9" * length))

def saving():
    try:
        save_choice = int(input("Would you like to save your password? Type 1 for yes, any other integer for no: "))
        if save_choice == 1:
            with open("passwords.txt", "a") as f:
                f.write(f"{pwd}\n")
            print("Password saved")
        else:
            print("Quitting program")
    except ValueError:
        print("Please input an integer")
        saving()
        
prompt()
generator()
saving()
print(f"Your password is {pwd}")

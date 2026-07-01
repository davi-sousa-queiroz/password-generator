import random
import time

passwords = []

password = []


def generate():
    time.sleep(1)
    password.clear()
    passwords.clear()
    print()
    for num in range(1, 11):
        single = random.randint(0, 9)
        password.append(single)
        passwords.append(single)
    for num in password:
        print(num, end="")
    print()


def intro():
    time.sleep(1)
    print("\n------------- WELCOME TO PASSWORD GENERATOR -----------")
    time.sleep(1)


def main_menu():
    print("\n1) Generate New Password")
    print("2) View Password")
    print("3) Create New Password")


def view_passwords():
    time.sleep(1)
    print()
    if passwords:
        for password in passwords:
            print(password, end="")
        print()
    else:
        print("\nYou Have No Set Password")


def create_password():
    time.sleep(1)

    passwords.clear()

    print("\nCreate Your Passsword!")

    created_password = input("\n>> ")

    passwords.append(created_password)

    print("\nPassword Set!")

    print()

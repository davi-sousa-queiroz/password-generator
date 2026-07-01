import random
import time

password = []


def generate():
    time.sleep(1)
    password.clear()
    print()
    for num in range(1, 11):
        single = random.randint(0, 9)
        password.append(single)
    for num in password:
        print(num, end="")
    print()


def intro():
    time.sleep(1)
    print("\n------------- WELCOME TO PASSWORD GENERATOR -----------")
    time.sleep(1)


def main_menu():
    print("1) Generate Password")
    print("2) View Passwords")
    print("3) Create Password")

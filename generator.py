import random
import time

password = []


def generate():
    for num in range(1, 11):
        single = random.randint(0, 9)
        password.append(single)


def intro():
    time.sleep(1)
    print("------------- WELCOME TO PASSWORD GENERATOR -----------")
    time.sleep(1)

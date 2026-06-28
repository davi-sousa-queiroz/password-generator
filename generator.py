import random

password = []


def generate():
    for num in range(1, 11):
        single = random.randint(0, 9)
        password.append(single)

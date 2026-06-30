from generator import generate
from generator import password
from generator import intro

while True:
    intro()
    generate()
    for num in password:
        print(num, end="")
    break

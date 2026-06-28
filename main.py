from generator import generate
from generator import password

while True:
    generate()
    for num in password:
        print(num, end="")
    print()
    break

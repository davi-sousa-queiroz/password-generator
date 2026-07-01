from generator import generate
from generator import intro
from generator import main_menu
from generator import view_passwords

intro()

while True:
    main_menu()
    selection = input("\n>>  ")
    if selection == "1":
        generate()
        print()
    elif selection == "2":
        view_passwords()

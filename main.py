from generator import generate
from generator import intro
from generator import main_menu

while True:
    intro()
    main_menu()
    selection = input("\n>>  ")
    if selection == "1":
        generate()

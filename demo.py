def menu(option):
    match option:
        case 1:
            print("You selected Add")
        case 2:
            print("You selected View")
        case 3:
            print("You selected Delete")
        case _:
            print("Invalid option")

choice = int(input("Enter option (1-3): "))
menu(choice)
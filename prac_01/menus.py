name = input("Enter name: ")


def display_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")


display_menus()

choice = input(">>> ").upper()

while choice != 'Q':
    if choice == 'H':
        print("Hello", name)
    elif choice == 'G':
        print("Goodbye", name)
    else:
        print("Invalid choice")

    display_menus()
    choice = input(">>> ").upper()

print("Finished.")

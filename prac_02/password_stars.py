def main():
    length = 0

    while length < 10:
        password = get_password()
        length = print_asterisks(password)
        if length < 10:
            print("Your password is weak!! Please choose a password with a minimum length of 10")
        else:
            print('*' * length)


def get_password():
    password = input("Enter your password: ")
    return password


def print_asterisks(password):
    length = len(password)
    return length


main()

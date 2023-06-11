def main():
    length = 0

    while length < 10:
        password = input("Enter your password: ")
        length = len(password)
        if length < 10:
            print("Your password is weak!! Please choose a password with a minimum length of 10")
        else:
            print('*' * length)
main()

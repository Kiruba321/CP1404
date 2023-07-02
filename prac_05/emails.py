def main():
    email_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_name[email] = name
        email = input("Email: ")

    for email, name in email_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract expected name from email address."""
    parts = email.split('@')[0].split('.')
    name = " ".join(parts).title()
    return name


main()

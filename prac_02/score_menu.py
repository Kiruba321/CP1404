def main():
    while True:
        print("\nMenu:")
        print("(I)nput score")
        print("(P)rint result")
        print("(Q)uit")

        choice = input("Enter: ").upper()

        if choice == "I":
            score = get_score()
        elif choice == "P":
            try:
                print("Result: " + find_status(score))
            except NameError:
                print("No score entered yet. Please choose option to enter a score (I) .")
        elif choice == "Q":
            print("Farewell!")
            break
        else:
            print("Invalid option. Please select a valid option.")


def get_score():
    while True:
        try:
            score = float(input("Enter a score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score. Please enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid score.")


def find_status(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()

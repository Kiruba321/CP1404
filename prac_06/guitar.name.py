class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"


def get_guitar_details():
    name = input("Name: ")
    if not name:
        return None

    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    return Guitar(name, year, cost)


def main():
    print("My guitars!")

    guitars = []
    guitar = get_guitar_details()
    while guitar is not None:
        guitars.append(guitar)
        print(f"{str(guitar)} added.")
        guitar = get_guitar_details()

    print("\nThese are my guitars:")
    for index, guitar in enumerate(guitars, 1):
        vintage_label = " (vintage)" if guitar.year <= 1973 else ""
        print(f"Guitar {index}: {str(guitar)}, worth ${guitar.cost:,.2f}{vintage_label}")


if __name__ == "__main__":
    main()
class Guitar:

    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}, {self.year}, ${self.cost:.2f}"

    def __lt__(self, other):
        return self.year < other.year


def read_guitars_from_file(filename):
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            year = int(year)
            cost = float(cost)
            guitars.append(Guitar(name, year, cost))
    return guitars


def write_guitars_to_file(filename, guitars):
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def main():
    filename = 'guitars.csv'
    guitars = read_guitars_from_file(filename)

    print("All guitars:")
    for guitar in guitars:
        print(guitar)

    user_input = input("Enter guitar name or 'exit' to finish: ")
    while user_input.lower() != 'exit':
        name = user_input
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))
        guitars.append(Guitar(name, year, cost))
        user_input = input("Enter guitar name or 'exit' to finish: ")

    guitars.sort()

    print("\nGuitars sorted by year (oldest to newest):")
    for guitar in guitars:
        print(guitar)

    write_guitars_to_file(filename, guitars)


if __name__ == "__main__":
    main()

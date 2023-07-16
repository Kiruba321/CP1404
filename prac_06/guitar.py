CURRENT_YEAR = 2017
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        return self.year < other.year

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Line 6 JTV-59", 2010, 1512.9)

print(guitar1)
print(f"The guitar is {guitar1.get_age()} years old.")
print(f"Is the guitar vintage? {guitar1.is_vintage()}")

print(guitar2)
print(f"The guitar is {guitar2.get_age()} years old.")
print(f"Is the guitar vintage? {guitar2.is_vintage()}")
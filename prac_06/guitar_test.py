class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year):
        return current_year - self.year

    def is_vintage(self, current_year):
        return self.get_age(current_year) >= 50


# Test the methods
def test_guitar_methods():
    gibson_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 1200)

    # Test get_age()
    print(f"{gibson_guitar.name} get_age() - Expected 100. Got {gibson_guitar.get_age(2022)}")
    print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age(2022)}")

    # Test is_vintage()
    print(f"{gibson_guitar.name} is_vintage() - Expected True. Got {gibson_guitar.is_vintage(2022)}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage(2022)}")


if __name__ == "__main__":
    test_guitar_methods()

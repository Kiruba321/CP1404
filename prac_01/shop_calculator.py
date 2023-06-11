
def validate_number_of_items():
    while True:
        try:
            number_of_items = int(input("Number of items: "))
            if number_of_items < 0:
                print("Invalid number of items!")
            else:
                return number_of_items
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculate_total_price(number_of_items):
    total_cost = 0
    for i in range(number_of_items):
        while True:
            try:
                price_of_item = float(input(f"Price of item {i+1}: $"))
                total_cost += price_of_item
                break
            except ValueError:
                print("Invalid input! Please enter a valid price.")

    return total_cost

number_of_items = validate_number_of_items()
total_price = calculate_total_price(number_of_items)

if total_price > 100:
    discount = total_price * 0.1
    total_price -= discount

print(f"Total price for {number_of_items} items is ${total_price:.2f}")
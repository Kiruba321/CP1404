numbers = [3, 1, 4, 1, 5, 9, 2]

# What values do the following expressions have?
# (solutions not provided; figure it out, then run with print or in console to test)
numbers[0]  # -> 3
numbers[-1]  # -> 2
numbers[3]  # -> 1
numbers[:-1]  # -> [3, 1, 4, 1, 5, 9]
numbers[3:4]  # -> [1]
5 in numbers  # -> True
7 in numbers  # -> False
"3" in numbers  # -> False
numbers + [6, 5, 3]  # -> [3, 1, 4, 1, 5, 9, 2, 6, 6, 5, 3]

# Write Python expressions (in your Python file) to achieve the following:

# Change the first element of numbers to "ten"
numbers[0] = "ten"
# Change the last element of numbers to 1
numbers[-1] = 1
# Print all elements from numbers except the firs two
print(numbers[2:])
# Check if 9 is an element of numbers
print(9 in numbers)

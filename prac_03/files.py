# Q1
output_file = 'name.TXT'
out_file = open(output_file, 'w')  # open file for writing
name = input('Enter your name: ')
print('you name is: ', name, file=out_file)
out_file.close()


# Q2
open_file = open("name.txt", "r")
name = open_file.read().strip()
print("Your name is", name)
open_file.close()


# Q3
open_file = open("numbers.TXT", "r")
first_line = int(open_file.readline())
second_line = int(open_file.readline())
result = first_line + second_line
print("Sum of line 1 & 2 is ",result)

a
# Q4
open_file = open("numbers.TXT", "r")
total = 0
for line in open_file:
    i = int(line)
    total += i
print("The sum of all lines are",total)
open_file.close()

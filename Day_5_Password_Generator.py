import random

upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_upper_letters = int(input("How many upper letters would you like in your password?\n"))
nr_lower_letters = int(input("How many lower letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for let in range(1, nr_upper_letters + 1):
    password.append(random.choice(upper_letters))

for let in range(1, nr_lower_letters + 1):
    password.append(random.choice(lower_letters))

for num in range(1, nr_numbers + 1):
    password += random.choice(numbers)

for sym in range(1, nr_symbols + 1):
    password += random.choice(symbols)

random.shuffle(password)

new_password = ""
for char in password:
    new_password += char

print(new_password)

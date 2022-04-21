print("Welcome to the tip calculator.\n")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_total = total_bill * (percentage / 100)
total_each = round((total_bill + tip_total) / people, 2)

print(f"Each person should pay: ${total_each}")

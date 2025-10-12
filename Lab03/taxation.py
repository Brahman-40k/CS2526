#   This program calculates the taxes according to:
#   1. martial status
#   2. income
#   Then prints the taxes accordingly.

user_input = input("Enter your martial status [unmarried (UM) or married (M)]: ")
user_input = user_input.lower()
income = int(input("Enter your income: $"))

# If user is unmarried
if user_input.lower() == "um":
    if income >= 0 and income <= 8000:
        taxes = 0.10 * income
    elif income > 8000 and income <= 32000:
        taxes = 800 + (0.15 * income)
    elif income > 32000:
        taxes = 4400 + (0.25 * income)

# If user is married
if user_input.lower() == "m":
    if income >= 0 and income <= 16000:
        taxes = 0.10 * income
    elif income > 16000 and income <= 64000:
        taxes = 1600 + (0.15 * income)
    elif income > 64000:
        taxes = 8800 + (0.25 * income)

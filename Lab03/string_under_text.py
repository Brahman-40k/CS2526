user_input = input("Enter a string of characters: ")

if user_input.isalpha():
    print("It only contains letters.")
if user_input.isupper():
    print("It contains only capital letters.")
if user_input.islower():
    print("It contains only lowercase letters.")
if user_input.isdecimal():
    print("It contains only decimal numeric digits.")
if user_input.isalnum():
    print("It contains only letter and digits.")
if user_input.istitle():
    print("It starts with a capital letter.")
if user_input.endswith("."):
    print("It ends with a point (.).")

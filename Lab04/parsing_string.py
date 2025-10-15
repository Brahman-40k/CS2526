user_input = input("Enter a string of characters: ")
# uppercase letters
print("These are the uppercase letters: ", end="")
for i in user_input:
    if i.isupper():
        print(i, end=",")
print()
# even position
print()
print("This are the letters in the even position of the string: ", end="")
for j in range(0, len(user_input), 2):
    if j % 2 == 0:
        print(user_input[j], end=",")
print()
# vowels replaced with '_' (underscores)
vowels = "aieouAIEOU"
new_vowel_string = ""
position_vowel = ""

for k in range(0, len(user_input)):
    if user_input[k] in vowels:
        new_vowel_string = new_vowel_string + "_"
        position_vowel = position_vowel + str(k)
    else:
        new_vowel_string = new_vowel_string + user_input[k]
print("The new string (vowels switched with '_') is: ", new_vowel_string)
print("The position of vowels are: ", position_vowel)
# number of numeric digits in the string
counter = 0
for l in user_input:
    if l.isdecimal:
        counter += 1
print("The number of numerical digits in the string is: ", counter)

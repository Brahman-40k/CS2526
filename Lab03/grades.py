# Grades

plus = 0.3
minus = -0.3
A = 4.0
B = 3.0
C = 2.0
D = 1.0
F = 0.0
user_input = input("Enter your grade: ")

user_input = user_input.upper()

if user_input == "A" or user_input == "A+":
    print(4.0)
elif user_input == "A-":
    print(A + minus)
elif user_input == "B+":
    print(B + plus)
elif user_input == "B":
    print(B)
elif user_input == "B-":
    print(B + minus)
elif user_input == "C+":
    print(C + plus)
elif user_input == "C":
    print(C)
elif user_input == "C-":
    print(C + minus)
elif user_input == "D+":
    print(D + plus)
elif user_input == "D":
    print(D)
elif user_input == "D-":
    print(D + minus)
elif user_input == "F":
    print(F)
else:
    print("Invalid grade entered.")
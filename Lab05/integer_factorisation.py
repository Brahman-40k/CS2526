number = abs(int(input("Enter an integer: ")))
i = 2
remainder = number
flag = True
while remainder > 1:
    if remainder % i == 0:
        print(i)
        remainder = remainder // i  # Gives the remainder
    else:
        i += 1

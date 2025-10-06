# five digit positive integer

var = input("Enter a five-digit positive integer: ")

while len(var) < 5 or len(var) > 5:
    if len(var) < 5:
        print("Too few digits! Try again")
        var = int(input("Enter a five-digit positive integer: "))
    else:
        print("Too many digits")
        var = int(input("Enter a five-digit positive integer: "))

for i in range(0, len(var)):
    print(var[i])

u_io = int(input("Enter an integer: "))
symbol = input("Enter a special character: ")
for i in range(u_io):
    for j in range(u_io):
        print(symbol, end=" ")
    print()

for k in range(u_io):
    print(" " * (u_io - 1 - k) + symbol * (2 * k + 1))

for l in range(u_io - 2, -1, -1):
    print(" " * (u_io - 1 - l) + symbol * (2 * l + 1))

# Random number generator

a = 32310901
b = 1729
m = 2**24

r_old = int(input("Enter a random number: "))
i = 0
while i < 100:
    r_new = ((a * r_old) + b) % m
    print(f"{r_new}")
    r_old = r_new
    i += 1


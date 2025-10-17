import random as rd

counter = 0
random_numbers = []
while counter < 10:
    value = rd.randint(1, 10)
    random_numbers.append(value)
    counter += 1
print("The elements of even index are: ", end="")
for i in range(len(random_numbers)):
    if i % 2 == 0:
        print(i, end=",")
print()
print("The elements of even value are: ", end="")
for j in random_numbers:
    if j % 2 == 0:
        print(j, end=",")
print()
print(random_numbers[::-1])
print(f"First element: {random_numbers[0]}\nLast element: {random_numbers[-1]}")

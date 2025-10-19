import random as rd

values = []
for i in range(10):
    values.append(rd.randint(1, 10))
largest = max(values)
for i in values:
    print("*" * int(40 * (i / largest)), f"{int(40 * (i / largest))}")

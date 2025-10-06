# two numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

add = a + b
diff = a - b
prod = a * b
avg = (a + b) / 2
dist = abs(a - b)
maxnum = max(a, b)
minnum = min(a, b)

print(f"Sum:           {add:>20}")
print(f"Difference:    {diff:>20}")
print(f"Product:       {prod:>20}")
print(f"Average Value: {avg:>20}")
print(f"Distance:      {dist:>20}")
print(f"Maximum Value: {maxnum:>20}")
print(f"Minimum Value: {minnum:>20}")

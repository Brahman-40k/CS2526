numbers = []
is_running = True
while is_running:
    a = input("Enter a number: ")
    if a == "":
        break
    numbers.append(int(a))
minimum = min(numbers)
maximum = max(numbers)
# Maximum and minimum removed from the list
task1 = []
for j in numbers:
    if j == maximum or j == minimum:
        continue
    else:
        task1.append(j)
# only even values
task2 = []
for k in numbers:
    if k % 2 == 0:
        task2.append(k)
# only tens values
task3 = []
for l in numbers:
    if l >= 10 and l <= 99:
        task3.append(l)
ts1 = []
ts2 = []
ts3 = []
for num in task1:
    ts1.append(str(num))
for num in task2:
    ts2.append(str(num))
for num in task3:
    ts3.append(str(num))
print(":".join(ts1))
print(":".join(ts2))
print(":".join(ts3))

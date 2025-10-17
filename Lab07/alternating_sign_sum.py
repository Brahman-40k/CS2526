is_running = True
numbers = []
while is_running:
    a = input("Enter a number: ")
    if a == "":
        break
    a = int(a)
    numbers.append(a)
even_sum = 0
odd_sum = 0
for i in range(len(numbers)):
    if i % 2 == 0:
        even_sum = even_sum + numbers[i]
    else:
        odd_sum = odd_sum + numbers[i]

print(even_sum - odd_sum)

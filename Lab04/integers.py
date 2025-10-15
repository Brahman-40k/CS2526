total = 0
is_running = True
counter_even = 0
counter_odd = 0
listt = []
while is_running:
    num = int(input("Enter an positive integer: "))
    if num == 0:
        break
    listt.append(num)
    if num % 2 == 0:
        counter_even += 1
    else:
        counter_odd += 1
    total = total + num
    print(total)
print(max(listt))
print(min(listt))
print(counter_even)
print(counter_odd)

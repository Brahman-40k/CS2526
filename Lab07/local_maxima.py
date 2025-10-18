v = []
is_running = True
while is_running:
    a = input("Enter a number: ")
    if a == "":
        break
    else:
        v.append(int(a))
print(v)

for i in range(1, len(v) - 1):
    if v[i - 1] < v[i] and v[i] > v[i + 1]:
        print(i,end=",")

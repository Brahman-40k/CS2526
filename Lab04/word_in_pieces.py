string1 = "rum"
n = len(string1)

for i in range(1, n + 1):
    for j in range(n - i + 1):
        print(string1[j : j + i])

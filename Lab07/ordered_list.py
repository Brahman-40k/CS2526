import random as rd

listt = []
i = 0
while i < 20:
    a = rd.randint(0, 99)
    listt.append(a)
    i += 1
listt.sort()
print(listt)

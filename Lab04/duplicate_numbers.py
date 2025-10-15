a = int(input("Enter a number: "))
words = ""
words += str(a)
flag = True
while flag:
    a = input("Enter a number: ")
    if a == "":
        break
    words += str(a)
    if int(words[-1]) == int(words[-2]):
        print(a)
    else:
        pass

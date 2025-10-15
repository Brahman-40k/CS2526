uio = input("Enter a string of characters: ")
result = ""
# I. reversed string
print(uio[::-1])
for i in uio:
    if i.isupper():
        result = result + i

print(result)

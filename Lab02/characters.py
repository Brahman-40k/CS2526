# characters.py

string = "Mississippi"
# print(string[0:3]+'...'+string[-3:])
if len(string) <= 3:
    print(string)
elif len(string) < 6:
    print(string[0:3] + "...")
else:
    print(string[0:3] + "..." + string[-3:])

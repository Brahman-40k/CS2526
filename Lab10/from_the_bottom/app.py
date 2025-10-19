try:
    with open("./input.txt", "r") as input:
        string = []
        for line in input:
            string.append(line)
except FileNotFoundError:
    print("The file does not exist!")

string = string[::-1]
try:
    with open("./output.txt", "w") as output:
        for i in string:
            output.write(i)
except FileNotFoundError:
    print("Unable to perform the write action.")

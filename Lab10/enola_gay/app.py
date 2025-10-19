try:
    outfile = open("output.txt", "w")
    with open("./input.txt", "r") as infile:
        counter = 1
        for line in infile:
            outfile.write(f"/*{counter}*/{line}")
            counter += 1
except FileNotFoundError:
    print("The file does not exist.")
outfile.close()

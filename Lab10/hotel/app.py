def main():
    try:
        with open("/home/mohan/CS2526/Lab10/hotel/input.txt", "r") as infile:
            dinner_total = 0
            lodging_total = 0
            for line in infile:
                line = line.strip()
                parts = line.split(";")
                if parts[1].lower() == "dinner":
                    dinner_total += float(parts[2])
                if parts[1].lower() == "lodging":
                    lodging_total += float(parts[2])
            print(f"The Total revenue made from dinners is ${dinner_total}.")
            print(f"The Total revenue made from dinners is ${lodging_total}.")
    except FileNotFoundError:
        print("The input file does not exist.")


main()

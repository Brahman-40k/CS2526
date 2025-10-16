def main():
    try:
        income = int(input("What is your yearly income: $"))
        children = int(input("How many children are there in your family: "))
        result = ngo(income,children)
        print(f"The financial aid you are qualified for is: {result}")
    except ValueError:
        print("Please fill in the appropriate values in the fields correctly: ")


def ngo(income, children):
    if income < 40000 and income >= 30000:
        if children >= 3:
            return 1000*children
        else:
            return 0
    if income < 30000 and income >= 20000:
        if children >= 2:
            return 1500*children
        else:
            return 0
    if income < 20000:
        return 2000 * children


if __name__ == "__main__":
    main()

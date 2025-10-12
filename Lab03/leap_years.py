# Leap Years


def leap_year(uio):

    while uio < 1582:
        print("Error! The year should be greater than 1582.")
        uio = int(input("Enter the year (>1582): "))

    if uio % 4 == 0 and not uio % 100 == 0:
        print("This year is a leap year!")
    elif uio % 400 == 0:
        print("This year is a leap year!")
    else:
        print("This is not a leap year.")


def main():
    uio = int(input("Enter the year ( > 1582): "))
    leap_year(uio)


if __name__ == "__main__":
    main()

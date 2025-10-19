# The price function now finds the first available seat for that price
# and modifies the list directly.
# 'i' is now the row index, 'j' is the column index
def price(seats, money):
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            # Check if the price matches AND the seat is not taken
            if seats[i][j] == money:
                seats[i][j] = 0  # This modifies the list!
                print(f"Success! Booked seat at row {i + 1}, column {j + 1}.")
                return  # Exit after finding the first seat

    # This line only runs if the loops finish
    print(f"Sorry, no seats available for ${money}.")


# The place function now checks the seat directly
# using the 'row' and 'column' indices. No loops needed!
def place(seats, row, column):
    # First, check if the seat is already taken
    if seats[row][column] == 0:
        print("already taken")
    else:
        # If not, get the price and then book it
        price = seats[row][column]
        seats[row][column] = 0  # This modifies the list!
        print(
            f"Success! Booked seat at row {row + 1}, column {column + 1} for ${price}."
        )


# A helper function to see the changes
def print_seats(seats):
    print("\nCurrent Seating Chart (0 = Taken):")
    for r in seats:
        for s in r:
            print(f"{s:>2}", end=" ")  # Format to line up
        print()  # Newline at end of row


def main():
    # seats is defined ONCE, outside the loop
    seats = [
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
        [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
        [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
        [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],
        [20, 30, 30, 40, 50, 50, 40, 30, 30, 20],
        [30, 40, 50, 50, 50, 50, 50, 50, 40, 30],
    ]
    print("Ciao, Welcome to the theatre")

    is_running = True
    # The loop now wraps the booking logic
    while is_running:

        # Show the current seats
        print_seats(seats)

        user_choice = input(
            "\nHow would you like to choose your seat by price($) or position(pos): "
        )

        if user_choice == "$":
            try:
                money = int(input("how much: "))
                price(seats, money)  # 'seats' list is modified
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Use 'elif' so it doesn't run after '$'
        elif user_choice.lower() == "pos":
            try:
                row = int(input("Enter the row (1-9): "))
                row -= 1  # Adjust to 0-based index
                col = int(input("Enter the column(1-10): "))
                col -= 1  # Adjust to 0-based index

                # Check if indices are valid
                if 0 <= row < len(seats) and 0 <= col < len(seats[0]):
                    place(seats, row, col)  # 'seats' list is modified
                else:
                    print("Invalid seat position. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        else:
            print("Invalid choice. Please enter '$' or 'pos'.")

        # Ask to continue at the end of the loop
        a = input("\nWould you like to continue(y/n): ")
        if a.lower() == "n" or a.lower() == "":
            is_running = False  # This will stop the loop

        # If 'y' (or anything else), the loop will just repeat

    print("Thank you for booking. Goodbye!")


if __name__ == "__main__":
    main()

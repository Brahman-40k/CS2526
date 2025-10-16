# ATM
print("Welcome to the ATM")
PIN = 1234
tries = 0
is_running = True
while is_running:
    uio = int(input("Enter your pin: "))
    if uio == PIN:
        print("Your PIN is correct")
        break
    # Records the no. of tries
    else:
        print("Your PIN is incorrect.")
        tries += 1
    # This if statement terminates the program and blocks the card
    if tries == 3:
        print("Your card is blocked")
        quit()
print("Thanks for using the ATM.\n" "See you again.")

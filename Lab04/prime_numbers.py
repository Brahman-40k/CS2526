# Ask the user for the upper limit.
limit = int(input("Enter an integer: "))

print(f"Prime numbers up to {limit} are:")

# Loop through each number from 2 up to the user's number.
for number in range(2, limit + 1):
    is_prime = True  # Assume the number is prime until proven otherwise.

    # Check for factors from 2 up to the square root of the number.
    # We only need to check this far for efficiency.
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False  # Found a factor, so it's not a prime number.
            break           # No need to check other factors, so exit the inner loop.

    # If is_prime is still True, it means no factors were found.
    if is_prime:
        print(number)
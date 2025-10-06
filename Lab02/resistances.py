# resistances

r1 = int(input("Enter the resistance R1: "))
r2 = int(input("Enter the resistance R2: "))
r3 = int(input("Enter the resistance R3: "))

print("Calculating the resistances...")
r23 = (r2 * r3) / (r2 + r3)

total_r = r1 + r23
print(f"The total resistance is: {total_r:.2f}")

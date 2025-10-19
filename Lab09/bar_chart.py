import random as rd

countries = [
    "United States",
    "Canada",
    "Brazil",
    "United Kingdom",
    "France",
    "Germany",
    "India",
    "China",
    "Australia",
    "South Africa",
]
values = []
for i in range(10):
    values.append(rd.randint(1, 10))
largest = max(values)

for i, j in zip(countries, values):
    bar = "*" * int(40 * (j / largest))
    print(f"{i}: {bar}")

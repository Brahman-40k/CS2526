# Table
n = int(input("Enter the no. of columns: "))
m = int(input("Enter the no. of rows: "))
table = []
# step I,II,III
for k in range(m):
    rows = []
    for l in range(n):
        rows.append(1)
    table.append(rows)
for i in range(len(table)):
    for j in range(len(table[i])):
        if i % 2 == 0:
            if j % 2 == 0:
                table[i][j] = 0
            else:
                table[i][j] = 1
        else:
            if j % 2 == 0:
                table[i][j] = 1
            else:
                table[i][j] = 0
# step IV
for a in range(len(table)):
    for b in range(len(table[a])):
        table[0][b] = 0
        table[-1][b] = 0
for x in range(len(table)):
    for y in range(len(table[x])):
        table[x][0] = 1
        table[x][-1] = 1
total = 0
for row in table:
    for column in row:
        total += column

print(total)

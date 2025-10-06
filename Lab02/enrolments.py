# enrollments

student_1 = input("Enter student 1's matricola: ")
student_2 = input("Enter student 2's matricola: ")

# printing in ascending order

s1 = int(student_1[1:])
s2 = int(student_2[1:])
first = min(s1, s2)
second = max(s1, s2)
print(f"{first}\n{second}")

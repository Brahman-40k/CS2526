def main():
    try:
        student_Id = input("Enter your student ID: ")
        file_classes = "/home/mohan/CS2526/Lab10/university_recod_book/classes.txt"
        with open(file_classes, "r") as in_file:
            for line in in_file:
                line = line.strip()
                try:
                    with open(
                        f"/home/mohan/CS2526/Lab10/university_recod_book/{line}.txt",
                        "r",
                    ) as subject:
                        for i in subject:
                            i = i.strip()
                            parts = i.split()
                            if parts[0] == student_Id:
                                print(f"{line}: {parts[1]}")
                except FileNotFoundError:
                    print("The relevant subject file could not be found.")

    except FileNotFoundError:
        print("The relevant input files were not found!")


main()

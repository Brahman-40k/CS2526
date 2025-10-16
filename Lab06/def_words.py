def main():
    string = input("Enter a string of characters: ")
    result = count_words(string)
    print(result)


def count_words(string):
    counter = 1
    for i in string:
        if i == " ":
            counter += 1
    return counter


if __name__ == "__main__":
    main()

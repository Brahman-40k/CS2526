# vowel counting function
def main():
    user_input = input("Enter a string of characters: ")
    result = count_vowels(user_input)
    print("The number of occurrences of vowels in your string are:", result)


def count_vowels(string):
    vowels = "aieouAIEOU"
    counter = 0
    for i in string:
        if i in vowels:
            counter += 1
    return counter


if __name__ == "__main__":
    main()

def count_words(filename):
    try:
        with open(filename, "r") as file:
            text = file.read().lower()
            words = text.split()
            word_count = {}
            for i in words:
                word_count[i] = word_count.get(i, 0) + 1
            for ik, jk in word_count.items():
                print(f"{ik}:{jk}")
    except FileNotFoundError:
        print("The input file could not be found.")


def main():
    filename = "/home/mohan/CS2526/Lab11/counting_words/input.text"
    count_words(filename)


main()

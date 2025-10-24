def main():
    try:
        with open("bad_words.txt", "r") as f_bad:
            bad_words_set = {line.strip() for line in f_bad}
    except FileNotFoundError:
        print("Error: 'bad_words.txt' not found.")
        exit()

    bad_words_sorted = sorted(bad_words_set, key=len, reverse=True)

    try:
        with open("raw_text.txt", "r") as f_raw:
            content = f_raw.read()
    except FileNotFoundError:
        print("Error: 'raw_text.txt' not found.")
        exit()

    for word in bad_words_sorted:
        asterisks = "*" * len(word)
        content = content.replace(word, asterisks)
    with open("censored_text.txt", "w") as f_censored:
        f_censored.write(content)

    print("File censored successfully and saved to 'censored_text.txt'.")


main()

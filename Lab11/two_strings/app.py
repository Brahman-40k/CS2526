def main():
    import string as st

    s1 = input("Enter a string: ")
    s2 = input("Enter a string: ")
    s1 = set(s1)
    s2 = set(s2)
    intersection = s1 & s2
    print(intersection)
    symmetric_difference = s1 ^ s2
    print(symmetric_difference)
    all_letters = set(st.ascii_letters.lower())
    # union
    print(all_letters - s1 | s2)  # '|' is the union operator


main()

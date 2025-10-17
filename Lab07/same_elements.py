def main():
    a = [1, 4, 9, 16, 9, 7, 4, 9, 11]
    b = [11, 11, 7, 9, 16, 4, 1]
    result = same_set(a, b)
    print(result)


def same_set(a, b):
    a = sorted(a)
    b = sorted(b)
    if len(a) != len(b):
        return False
    if a == b:
        return True
    else:
        return False


if __name__ == "__main__":
    main()

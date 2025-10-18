def main():
    import random as rd

    counter = 0
    v = []
    while counter < 10:
        a = rd.randint(0, 100)
        v.append(a)
        counter += 1
    v.sort()
    print("The original array:", v)
    print("The modified array:", remove_min(v))


def remove_min(v):
    v.sort()
    v.pop(0)
    return v


if __name__ == "__main__":
    main()

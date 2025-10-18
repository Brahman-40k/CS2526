def main():
    v = [1, 7, 9, 3, 0, 4]
    result = shiftList(v)
    print(v)
    print(result)


def shiftList(v):
    new_v = []
    new_v.append(v[-1])
    for i in range(len(v) - 1):
        new_v.append(v[i])
    return new_v


if __name__ == "__main__":
    main()

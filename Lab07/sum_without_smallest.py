def main():
    import random

    v = []
    counter = 0
    while counter < 10:
        a = random.randint(1, 100)
        v.append(a)
        counter += 1
    print("The sum of the original array", sum(v))
    result = sum_without_smallest(v)
    print(sum(result))


def sum_without_smallest(v):
    v.sort()
    v.remove(v[0])
    return v


if __name__ == "__main__":
    main()

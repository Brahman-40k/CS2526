def main():
    import random as rd

    v = []
    for i in range(10):
        v.append(rd.randint(0, 100))
    print("original array:", v)
    print("Swapped first and last item:", swap_first_last(v))
    print("Sliding the elements by one place:", shiftList(v))
    print("Replacing even values with 0:", replace_even_zero(v))
    print(
        "Replacing all elements with the larger extreme values:", replace_larger_0__1(v)
    )
    print(del_middle_element(v))
    print("even items on top and odd below:", even_top_odd_bottom(v))
    print("Second Largest Value:", second_largest_value(v))
    print("sorted list T/F:", sorted_ascending_boolean(v))
    print("Duplicate adjacent items:", duplicate_adjacent_items(v))
    print("Duplicate items", duplicate_items(v))


# This function swaps first element with the last one.
def swap_first_last(v):
    new = []
    for i in v:
        new.append(i)
    new[0] = v[-1]
    new[-1] = v[0]
    return new


# This function shifts all the elements of the array by one place
# and takes the last element to the first place of the new array.
def shiftList(v):
    new = []
    new.append(v[-1])
    for i in range(len(v) - 1):
        new.append(v[i])
    return new


def replace_even_zero(v):
    new = []
    new = v.copy()
    result = []
    for i in range(len(new)):
        if new[i] % 2 == 0:
            result.append(0)
        else:
            result.append(new[i])
    return result


def replace_larger_0__1(v):
    new = []
    new = v.copy()
    larger_value = max(new[0], new[-1])
    for i in range(1, len(new) - 1):
        new[i] = larger_value
    return new


def del_middle_element(v):
    new = []
    new = v.copy()
    if len(new) % 2 == 0:
        min_index = int(len(new) // 2)
        max_index = min_index - 1
        del new[min_index]
        del new[max_index]
    else:
        del new[int(len(new) / 2)]
    return new


def even_top_odd_bottom(v):
    por = []
    por = v.copy()
    even_top = []
    odd_top = []
    concatenated_string = []
    for i in range(len(por)):
        if por[i] % 2 == 0:
            even_top.append(por[i])
        else:
            odd_top.append(por[i])
    concatenated_string = even_top + odd_top
    return concatenated_string


def second_largest_value(v):
    new = v.copy()
    new.sort()
    return new[-2]


def sorted_ascending_boolean(v):
    new = v.copy()
    return True if new.sort() == v else False


def duplicate_adjacent_items(v):
    new = v.copy()
    for i in range(len(new) - 1):
        if new[i] == new[i + 1]:
            return True
    else:
        return False


def duplicate_items(v):
    return len(v) != len(set(v))


if __name__ == "__main__":
    main()

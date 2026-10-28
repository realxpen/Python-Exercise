Input1 = [10, 5, 8, 20, 15]
Input2 = [4, 9, 2, 9, 7]


def second_largest(values):
    largest = None
    second = None

    for number in values:
        if number == largest or number == second:
            continue

        if largest is None or number > largest:
            second = largest
            largest = number

        elif second is None or number > second:
            second = number

    return second


print(second_largest(Input1))
print(second_largest(Input2))
numbers = [[2, 7, 11, 15],
           [3, 8, 4, 6]]


def two_sum(values, target):
    # Check every pair of different positions in the list.
    for first_index in range(len(values)):
        for second_index in range(first_index + 1, len(values)):
            # Return the indexes when the pair adds up to the target.
            if values[first_index] + values[second_index] == target:
                return [first_index, second_index]


targets = [9, 7]

for values, target in zip(numbers, targets):
    print(two_sum(values, target))



from intersection import intersection

tests = [
    ([3, 4], [1, 2, 3, 4], [3, 4, 5, 6]),         # example from the problem
    ([], [1, 2], [3, 4]),                         # nothing in common
    ([], [], [1, 2]),                             # a is empty
    ([], [1, 2], []),                             # b is empty
    ([], [], []),                                 # both empty
    ([1, 2, 3], [1, 2, 3], [1, 2, 3]),            # identical lists
    ([5], [5], [5]),                              # single element
    ([2, 3], [1, 2, 2, 3], [2, 2, 3]),            # duplicates in both, each appears once
    ([2], [1, 2], [2, 2, 2]),                     # duplicates only in b
    ([3, 1], [3, 1, 2], [1, 3]),                  # order follows a, not b
    (["a", "c"], ["a", "b", "c"], ["c", "a"]),    # strings
    ([-1, 0], [-1, 0, 2], [0, -1, 3]),            # negatives and zero
]

failures = 0

for expected, a, b in tests:
    a_before, b_before = list(a), list(b)
    got = intersection(a, b)
    if got != expected:
        failures += 1
        print(f"FAIL: intersection({a_before}, {b_before})")
        print(f"  expected: {expected}")
        print(f"  got:      {got}\n")
    elif a != a_before or b != b_before:
        failures += 1
        print(f"FAIL: intersection({a_before}, {b_before}) mutated its input\n")

print("BIM!!!" if failures == 0 else f"{failures} failed")
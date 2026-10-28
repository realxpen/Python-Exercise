from missing_number import find_missing

tests = [
    (4, [1, 2, 3, 5, 6]),        # example from the problem
    (2, [1, 3]),                 # smallest valid input
    (3, [1, 2, 4, 5]),
    (7, [5, 6, 8, 9]),           # doesn't start at 1
    (0, [-2, -1, 1, 2]),         # negatives crossing zero
    (51, [48, 49, 50, 52, 53]),  # larger numbers
]

failures = 0

for expected, nums in tests:
    got = find_missing(nums)
    if got != expected:
        failures += 1
        print(f"FAIL: find_missing({nums})")
        print(f"  expected: {expected}")
        print(f"  got:      {got}\n")

print("BIM!!!" if failures == 0 else f"{failures} failed")
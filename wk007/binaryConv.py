n_input = int(input("Input a Number Only for Binary Conversion: "))

binary = ""

exact_input = n_input

while n_input > 0:

    remainder = n_input % 2
    remainder = str(remainder)
    # reversed_remainder = remainder[::-1]
    n_input = n_input // 2
    binary = remainder + binary #reversed it like this
print('Input:',exact_input,'--> Output:',binary)

    



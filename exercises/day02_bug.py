def binary_to_decimal(binary_str):
    total = 0
    for digit in binary_str:
        total = total * 2 + int(digit)   # <-- something about place value is missing
    return total

print(binary_to_decimal("1101"))   # prints 3, but 1101 should be 13

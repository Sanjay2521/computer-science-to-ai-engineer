def binary_to_decimal(binary_str: str) -> int:
    """Convert a binary string like '1101' to its decimal int value (13)."""
    # Your code here. Think place values (section 4.4).
    # Hint to get unstuck (don't read unless needed): walk the string left to right,
    # keep a running total, and for each new digit do: total = total * 2 + digit.
    ...
    total = 0
    for i in binary_str:
        total = total * 2 + int(i)
    return total



# Test cases — these should all pass when you're done:
assert binary_to_decimal("0") == 0
assert binary_to_decimal("1") == 1
assert binary_to_decimal("101") == 5
assert binary_to_decimal("1101") == 13
assert binary_to_decimal("11111111") == 255
print("binary_to_decimal: all tests passed")


def decimal_to_binary(n: int) -> str:
    """Convert a non-negative int like 13 to its binary string ('1101')."""
    # Your code here. Think: divide by 2, collect remainders, reverse (section 4.5).
    # Remember your prediction in Q4 — the number 0 is a special case.
    ...
    binary = ""
    if n == 0:
        return "0"
    else:

        while n > 0:
            remainders = n % 2
            binary = binary + str(remainders)
            n = n // 2
        return binary[::-1]



# Test cases:
assert decimal_to_binary(0) == "0"
assert decimal_to_binary(1) == "1"
assert decimal_to_binary(5) == "101"
assert decimal_to_binary(13) == "1101"
assert decimal_to_binary(255) == "11111111"
print("decimal_to_binary: all tests passed")



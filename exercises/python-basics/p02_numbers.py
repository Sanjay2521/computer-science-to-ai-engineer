# ============================================================
# P2 — numbers & operators
# ============================================================
#
# ---- TEACH (study this, then run the file) ----
#
# Python does math with these operators:
#
#     +   add            7 + 3   -> 10
#     -   subtract       7 - 3   -> 4
#     *   multiply       7 * 3   -> 21
#     /   divide         7 / 2   -> 3.5     (always gives a decimal / "float")
#     //  floor divide   7 // 2  -> 3       (whole-number quotient, drops the remainder)
#     %   modulo         7 % 2   -> 1       (the remainder after dividing)
#     **  power          2 ** 3  -> 8       (2 to the power 3)

a = 17
b = 5
print("a + b =", a + b)     # -> 22
print("a / b =", a / b)     # -> 3.4   (a float, note the decimal point)
print("a // b =", a // b)   # -> 3     (how many whole 5s fit in 17)
print("a % b =", a % b)     # -> 2     (what's left over: 17 = 5*3 + 2)
print("2 ** 8 =", 2 ** 8)   # -> 256   (remember this number from Day 2!)

# WHY // and % matter: together they split a number into "quotient and remainder".
# That's EXACTLY the repeated-division trick you'll use in the converter later.
#
# Run it:
#     python exercises/python-basics/p02_numbers.py
#
# ============================================================
# ---- PRACTICE (you write these) ----
# ============================================================

# Problem 1:
# A rectangle has width = 8 and height = 5 (make them variables).
# Print its area like:  Area: 40
# your code here
width = 8
height = 5 
print("Area of rectangle: ", height*width)


# Problem 2:
# Make two variables x = 17 and y = 5.
# Print the result of NORMAL division x / y, and look at the output.
# Then in a comment below your code, write: is it a whole number or a decimal?
# your code here
x = 17
y = 5
print("x / y =", x / y)


# Problem 3:
# Using the SAME x = 17 and y = 5:
# Print the quotient (x // y) and the remainder (x % y) on two lines, like:
#     Quotient: 3
#     Remainder: 2
# your code here
print("x // y =", x // y)
print("x % y =", x % y) 


# Problem 4 (tiny challenge):
# You have total_seconds = 125.
# Using // and %, print how many whole minutes that is and how many seconds are left over:
#     2 minutes and 5 seconds
# (Hint: 1 minute = 60 seconds. Which operator gives whole minutes? Which gives the leftover?
#  Attempt first; ask for a HINT only if stuck.)
# your code here
total_seconds = 125
minutes = total_seconds // 60
seconds = total_seconds % 60
print(f"{minutes} minutes and {seconds} seconds")



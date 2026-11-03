# ============================================================
# P5 — if / elif / else  (making decisions)
# ============================================================
#
# ---- TEACH (study this, then run the file) ----
#
# Programs make decisions by COMPARING values. Comparisons give True or False:
#
#     ==   equal to          5 == 5   -> True   (two = signs! one = is "assign")
#     !=   not equal to      5 != 3   -> True
#     <    less than         3 < 5    -> True
#     >    greater than      3 > 5    -> False
#     <=   less or equal     5 <= 5   -> True
#     >=   greater or equal  5 >= 6   -> False
#
# An if-statement runs a block ONLY when its condition is True:
#
#     if condition:
#         <-- these INDENTED lines run only if condition is True
#     elif other_condition:   # "else if" - checked only if the first was False
#         ...
#     else:                   # runs if none of the above were True
#         ...
#
# !! INDENTATION MATTERS in Python. The indented lines (4 spaces) belong to the
#    block above them. This is how Python knows what's "inside" the if.

temperature = 30

if temperature > 35:
    print("It's hot")
elif temperature > 20:
    print("It's pleasant")      # this one runs (30 is not > 35, but is > 20)
else:
    print("It's cold")

# Note: only ONE branch runs - the first condition that is True wins.
#
# Run it:
#     python exercises/python-basics/p05_conditionals.py
#
# ============================================================
# ---- PRACTICE (you write these) ----
# ============================================================

# Problem 1:
# Make a variable number = 7 (try other values later too).
# Print "positive" if it's > 0, "negative" if it's < 0, or "zero" otherwise.
# Use if / elif / else.
# your code here
number = 7 
if number > 0 :
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")


# Problem 2:
# Make a variable age = 20.
# If age is 18 or more, print "adult". Otherwise print "minor".
# your code here
age = 20 
if age >= 18:
    print("adult")
else:
    print("minor")


# Problem 3:
# Make a variable n = 10.
# Print "even" if n is even, "odd" if not.
# (Hint: a number is even when n % 2 == 0. You used % in P2!)
# your code here
n = 10 
if n % 2 == 0 :
    print("even")
else:
    print("odd")


# Problem 4 (tiny challenge):
# Make a variable score = 72 (a test score from 0 to 100).
# Print a grade using this scale:
#     90 or above  -> "A"
#     80 to 89     -> "B"
#     70 to 79     -> "C"
#     below 70     -> "F"
# (Hint: an elif chain, checking from the highest cutoff down. Attempt first; HINT if stuck.)
# your code here
score = 89
if score >= 90:
    print("A")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
else:
    print("F")

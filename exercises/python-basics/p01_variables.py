# ============================================================
# P1 — print & variables
# ============================================================
#
# ---- TEACH (study this worked example, then run the file) ----
#
# A VARIABLE is a labelled box that holds a value. You put a value in with "=".
# print(...) shows something on the screen.

name = "Sanjay"          # store the text "Sanjay" in a box called `name`
print("Hello,", name)    # -> Hello, Sanjay

age = 25                 # a box can hold a number too
print("Age:", age)       # -> Age: 25

# Notes:
#  - Text values go in quotes: "Sanjay". Numbers don't: 25.
#  - print can take several things separated by commas; it adds a space between them.
#  - The box name is yours to choose, but use clear names (age, city) not (x, q).
#
# Run this file now to see the two lines above print:
#     python exercises/python-basics/p01_variables.py
#
# ============================================================
# ---- PRACTICE (you write these — delete each `pass` and add your code) ----
# ============================================================

# Problem 1:
# Make a variable called `city` holding the city you live in, then print:
#     I live in <city>
# (It should print your real city, using the variable — not a hard-coded sentence.)
# your code here
city = "Bengaloure"
print(f"I live in {city}")


# Problem 2:
# Make two variables: `first` (your first name) and `last` (your last name).
# Print them on one line so it reads like:  Sanjay <last>
# your code here
first = "Sanjay"
last = "B M"
print(f"{first} {last}")


# Problem 3:
# Make a variable `year_born` holding the year you were born (a number).
# Print a line like:  I was born in <year_born>
# your code here
year_born = 2001
print("I was born in", year_born)


# Problem 4 (tiny challenge):
# Make a variable `favorite_number` with any number you like.
# Print TWO lines:
#     My favorite number is <favorite_number>
#     Double it is <favorite_number * 2>
# (Hint: you can do math right inside print, e.g. print(favorite_number * 2).
#  Attempt it first — ask me for a HINT only if stuck.)
# your code here
favorite_number = 6
print("My favorite number is ", favorite_number)
print("Double it is ", favorite_number * 2)

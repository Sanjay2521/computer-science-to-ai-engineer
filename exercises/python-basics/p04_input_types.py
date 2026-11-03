# ============================================================
# P4 — input & types  (the most important beginner gotcha!)
# ============================================================
#
# ---- TEACH (study this carefully, then run the file) ----
#
# input(...) PAUSES the program and lets the user type something.
# !! input ALWAYS gives you back a STRING -- even if the user types a number. !!
#
# type(x) tells you what kind of value x is.
#   type("hi")  -> <class 'str'>     (string / text)
#   type(5)     -> <class 'int'>     (whole number)
#   type(3.4)   -> <class 'float'>   (decimal number)
#
# To turn text into a number you must CONVERT it:
#   int("5")   -> 5      (string -> int)
#   float("3.4") -> 3.4  (string -> float)
#   str(5)     -> "5"    (number -> string)

# --- The classic trap (study, don't skip) ---
a = "2"            # this is a STRING, not the number 2
b = "3"
print(a + b)       # -> "23"  (strings glue together, they don't add!)  <-- remember Day 1?
print(int(a) + int(b))   # -> 5   (convert to int first, THEN they add)

# --- input example (this one WAITS for you to type) ---
# Run the file and type your name when it stops:
your_name = input("What is your name? ")      # whatever you type is a string
print("Hello,", your_name)

# To do MATH on typed input, convert it:
age_text = input("How old are you? ")          # e.g. you type 25 -> age_text is "25"
age = int(age_text)                            # now it's the number 25
print("Next year you'll be", age + 1)

# Run it (it will stop and wait for you to type):
#     python exercises/python-basics/p04_input_types.py
#
# ============================================================
# ---- PRACTICE (you write these) ----
# ============================================================

# Problem 1:
# Ask the user for their favourite colour with input(...).
# Then print:  Nice! <colour> is a great colour.
# your code here
user_colour = input("Whats your favourite colour: ")
print(f"Nice! {user_colour} is a great colour")

# Problem 2  (the key one):
# Ask the user for TWO numbers (two separate input calls).
# Print their SUM as a number.
# WARNING: if you forget to convert, "2" + "3" becomes "23", not 5. Convert with int()!
# your code here
user_input_1 = input("Enter a first number: ")
user_input_2 = input("Enter a second number: ")
print(int(user_input_1) + int(user_input_2))



# Problem 3:
# Create three variables: a word (string), a whole number (int), a decimal (float).
# Print the type() of each one, so you can SEE the three types.
# your code here
string_var = "Sanjay"
whole_var = 1
decimal = 1.3
print(type(string_var))
print(type(whole_var))
print(type(decimal))



# Problem 4 (tiny challenge):
# Ask the user for the current year (a number) and the year they were born (a number).
# Print their age like:  You are <age> years old.
# (Hint: age = current_year - birth_year, but remember both inputs arrive as STRINGS.
#  Attempt first; ask for a HINT only if stuck.)
# your code here
current_year = input("Enter the current year: ")
born_year = input("Enter the born year: ")
print(f"You are {int(current_year) - int(born_year)} years old")

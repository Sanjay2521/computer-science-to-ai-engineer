# ============================================================
# P3 — strings
# ============================================================
#
# ---- TEACH (study this, then run the file) ----
#
# A STRING is text in quotes: "hello". Python gives strings some handy tools:
#
#   +            glue (concatenate) strings     "ab" + "cd"  -> "abcd"
#   len(s)       how many characters            len("hello") -> 5
#   s[0]         the character at a position     "hello"[0]  -> "h"   (counting starts at 0!)
#   s[1]         the next character              "hello"[1]  -> "e"
#   s[-1]        the LAST character              "hello"[-1] -> "o"
#   s.upper()    a NEW upper-case copy           "hi".upper() -> "HI"
#   s.lower()    a NEW lower-case copy           "HI".lower() -> "hi"

word = "python"
print("glued:", "py" + "thon")     # -> python
print("length:", len(word))        # -> 6
print("first char:", word[0])      # -> p   (position 0, not 1!)
print("last char:", word[-1])      # -> n
print("shout:", word.upper())      # -> PYTHON

# KEY IDEA — positions start at 0. In "python": p=0, y=1, t=2, h=3, o=4, n=5.
# (This 0-based counting trips up every beginner. Burn it in now.)
#
# Run it:
#     python exercises/python-basics/p03_strings.py
#
# ============================================================
# ---- PRACTICE (you write these) ----
# ============================================================

# Problem 1:
# Make variables first = "Sanjay" and last = "B M".
# Using the + operator (NOT an f-string this time), build a variable `full`
# that is "Sanjay B M" (remember to glue a space " " in the middle), then print it.
# your code here


# Problem 2:
# Make a variable `word` = "computer".
# Print how many characters it has, like:  Length: 8
# your code here


# Problem 3:
# Using the SAME word = "computer":
# Print its FIRST character and its LAST character on two lines:
#     First: c
#     Last: r
# (Hint: positions start at 0; there's a handy index for the last one.)
# your code here


# Problem 4 (tiny challenge):
# Make a variable `name` with your name in normal case, e.g. "sanjay".
# Print it THREE ways on three lines: as-is, all UPPER case, and all lower case.
# (Hint: .upper() and .lower() give you back a new string — print those.)
# your code here

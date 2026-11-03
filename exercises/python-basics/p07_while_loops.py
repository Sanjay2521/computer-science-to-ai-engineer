# ============================================================
# P7 — while loops  (repeat until a condition stops being true)
# ============================================================
#
# ---- TEACH (study this, then run the file) ----
#
# A for-loop repeats a KNOWN number of times. A while-loop repeats as long as a
# condition stays True -- you use it when you don't know the count in advance.
#
#     while condition:
#         <-- these lines run over and over, UNTIL the condition becomes False
#
# You must change something inside the loop so the condition eventually becomes
# False -- otherwise it runs forever (an "infinite loop").

count = 5
while count > 0:          # keep going while count is still above 0
    print("count =", count)
    count = count - 1     # <-- this is what eventually ENDS the loop (5->4->3->2->1->0)
print("liftoff!")

# Watch the halving pattern below -- it's the exact shape of decimal_to_binary:
n = 13
while n > 0:
    print("n is now", n)
    n = n // 2            # 13 -> 6 -> 3 -> 1 -> 0, then the loop stops
print("done")

# !! If you forget to change the variable in the condition, the loop NEVER ends.
#    If a run hangs forever, press Ctrl+C to stop it.
#
# Run it:
#     python exercises/python-basics/p07_while_loops.py
#
# ============================================================
# ---- PRACTICE (you write these) ----
# ============================================================

# Problem 1:
# Using a WHILE loop (not for), count down from 10 to 1, each on its own line.
# (Hint: start a variable at 10, print it, subtract 1 each time, stop when it hits 0.)
# your code here


# Problem 2:
# Using a while loop, print the powers of 2 (1, 2, 4, 8, 16, ...) that are 100 or less.
# (Hint: start at 1, print it, then double it each time; keep going while it's <= 100.)
# your code here


# Problem 3:
# Start with number = 100. Using a while loop, keep subtracting 7 and printing the
# result, as long as the number stays above 0. (You don't know the count in advance -
# that's why while fits.)
# your code here


# Problem 4 (tiny challenge -- this previews the converter!):
# Make n = 13. While n is greater than 0:
#     print  n % 2   (the remainder when divided by 2 -- this is a binary digit!)
#     then set n = n // 2
# Look at the remainders you printed (bottom to top) -- do they spell 13 in binary (1101)?
# (Attempt first; HINT if stuck. This is literally how decimal->binary works.)
# your code here

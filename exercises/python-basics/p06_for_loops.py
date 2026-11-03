# ============================================================
# P6 — for loops & range  (doing something many times)
# ============================================================
#
# ---- TEACH (study this, then run the file) ----
#
# A for-loop repeats a block once for each item in a collection.
#
#   range(n)       gives the numbers 0, 1, 2, ... n-1   (stops BEFORE n!)
#     range(5)     -> 0 1 2 3 4
#   range(a, b)    gives a, a+1, ... b-1
#     range(1, 6)  -> 1 2 3 4 5
#
# Loop over a range of numbers:
for i in range(5):        # i takes the values 0,1,2,3,4 one at a time
    print("i is", i)

# A very common pattern: an ACCUMULATOR (build up a result as you loop)
total = 0
for n in range(1, 6):     # 1,2,3,4,5
    total = total + n     # keep adding each number to total
print("sum 1..5 =", total)   # -> 15

# You can also loop over the characters of a STRING:
for char in "cat":
    print("char:", char)   # -> c, then a, then t   (this is how the converter walks digits!)

# !! range(5) stops BEFORE 5 (gives 0-4). This off-by-one bites everyone - stay alert.
#
# Run it:
#     python exercises/python-basics/p06_for_loops.py
#
# ============================================================
# ---- PRACTICE (you write these) ----
# ============================================================

# Problem 1:
# Print the numbers 1 to 10, each on its own line.
# (Hint: what range gives 1..10? Remember it stops BEFORE the end value.)
# your code here


# Problem 2:
# Add up all the numbers from 1 to 100 and print the total.
# (Hint: the accumulator pattern above. The answer is 5050.)
# your code here


# Problem 3:
# Loop over the word "python" and print each character on its own line.
# your code here


# Problem 4 (tiny challenge):
# Count how many EVEN numbers there are from 1 to 20, and print the count.
# (Hint: loop 1..20, use an if with % 2 == 0, and keep a counter you add 1 to.
#  Expected answer: 10. Attempt first; HINT if stuck.)
# your code here

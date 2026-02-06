# CODE SOLUTION:
def rectangular_star_pattern(n):
    for i in range(1, n + 1):
        print("*" * n)


rectangular_star_pattern(3)


# INTUITION:
# A rectangular star pattern consists of N rows, where each row contains exactly N stars.
# So the problem reduces to printing one row of N stars, N times.


# WHY BRUTE FORCE FAILS:
# There is no simpler brute force alternative here since every star must be printed.
# Any solution must output N × N characters, which already enforces O(n^2) time.


# APPROACH:
# Use a loop that runs N times for the rows.
# In each iteration, print N stars in a single line.

# TIME COMPLEXITY:
# O(n^2) because N rows are printed and each row contains N stars.

# SPACE COMPLEXITY:
# O(1) because no extra data structures are used.

# EDGE CASES:
# N = 0 - nothing is printed

# WHAT I'D SAY IN AN INTERVIEW:
# Since every star must be printed, the time complexity cannot be better than O(n^2).
# The logic is straightforward: repeat a string of N stars for N rows.

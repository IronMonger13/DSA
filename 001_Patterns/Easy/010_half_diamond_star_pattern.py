"""
INTUITION:
Print half diamond for n number of rows, where stars increase from 1 to n then decrease to 1.


APPROACH:
Start a loop from 1 to n and then n-1 to 1. Second loop starts from n-1 as we dont have to duplicate nth row in the pattern.
For each row, print row index number of stars.


EDGE CASES:
n = 0 - nothing is printed.
"""


# CODE SOLUTION:
def half_diamond_star_pattern(n):
    for row in range(1, n + 1):
        print("*" * row)

    for row in range(n - 1, 0, -1):
        print("*" * row)


half_diamond_star_pattern(3)


"""
TIME COMPLEXITY:
O(n^2) since number of stars to be printed is 1 + 2 + ... + n + n-1 + ... + 2 + 1, which grows with order of n^2.


SPACE COMPLEXITY:
O(1) since no additional data structures were used, so no additional space is counted.


WHY BRUTE FORCE FAILS:
Brute force is already efficient since all stars need to be printed.


WHAT I'D SAY IN AN INTERVIEW:
This pattern forms a half-diamond where the number of stars increases from 1 to n and then decreases back to 1.
We iterate over two loops, the first builds the increasing part, and the second builds the decreasing part while avoiding duplication of the middle row.
The time complexity is O(n^2) because the total number of stars printed grows quadratically with n, which is unavoidable since every star must be printed.
"""

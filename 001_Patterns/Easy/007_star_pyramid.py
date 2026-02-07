"""
INTUITION:
This is a centered pyramid.
Each row has stars in the middle.
As the row number increases, the number of stars increases and the leading spaces decrease.


APPROACH:
Run a loop from 1 to n to control the rows.
For each row:
- Print (n - row) spaces to center the stars.
- Print (2 * row - 1) stars.
Print everything on the same line.

EDGE CASES:
n = 0 - nothing is printed.
"""


# CODE SOLUTION:
def star_pyramid(n):
    for row in range(1, n + 1):
        spaces = n - row
        stars = (2 * row) - 1
        print(" " * spaces + "*" * stars)


star_pyramid(5)


"""
TIME COMPLEXITY:
O(n^2) since number of stars grows with n.


SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force is acceptable since all stars need to be printed and no steps can be reduced.


WHAT I'D SAY IN AN INTERVIEW:
Each row is centered using spaces, and the number of stars follows the formula (2 * row - 1).
As rows increase, spaces decrease and stars increase.
The time complexity is unavoidable because all stars must be printed.
"""

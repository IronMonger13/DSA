"""
INTUITION:
This problem prints an inverted, center-aligned star pyramid.
The first row has the maximum number of stars, and each next row has two fewer stars.
Spaces are added in front to keep the pyramid centered.


APPROACH:
Run a loop from n down to 1 to control the rows.
For each row:
- Calculate stars as (2 * row - 1).
- Calculate spaces as (n - row).
- Print spaces followed by stars on the same line.


EDGE CASES:
n = 0 - nothing is printed.
"""


# CODE SOLUTION:
def inverted_star_pyramid(n):
    for row in range(n, 0, -1):
        star = 2 * row - 1
        space = n - row
        print(" " * space + "*" * star)


inverted_star_pyramid(5)


"""
TIME COMPLEXITY:
O(n^2) since number of stars to print increases with n.


SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force is acceptable since all stars need to be printed, and hence work or logic cannot be reduced.


WHAT I'D SAY IN AN INTERVIEW:
Each row prints a centered set of stars.
As we move down the pyramid, the number of stars decreases and spaces increase.
Since all stars must be printed, the time complexity is unavoidable.
"""

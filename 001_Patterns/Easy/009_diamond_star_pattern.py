"""
INTUITION:
Print a diamond pattern, which is a centred and inverted centred triangle stacked together.
First half is printing centred triangle for n rows, and second half is printing inverted centred triangle for n rows.


APPROACH:
For centred pyramid, start a loop from 1 to n, and for inverted centred traingle, start a loop from n to 1.
Inside both loops:
- Calculate number of spaces as n - row_index for each row.
- Calculate number of stars as 2 * row_index - 1 for each row.
- Print " " * spaces + "*" * stars for each row


EDGE CASES:
n = 0 - nothing is printed.
"""


# CODE SOLUTION:
def diamond_star_pattern(n):
    for row in range(1, n + 1):
        spaces = n - row
        stars = 2 * row - 1
        print(" " * spaces + "*" * stars)

    for row in range(n, 0, -1):
        spaces = n - row
        stars = 2 * row - 1
        print(" " * spaces + "*" * stars)


diamond_star_pattern(1)


"""
TIME COMPLEXITY:
O(n^2) since total number of stars to be printed increases quadratically with n.


SPACE COMPLEXITY:
O(1) since no additional data structures were used, so no extra space was taken.


WHY BRUTE FORCE FAILS:
Brute force is acceptable here since there is no alternative approach because every character of the pattern has to be printed.


WHAT I'D SAY IN AN INTERVIEW:
This pattern is a diamond formed by combining a centered pyramid and an inverted centered pyramid.
For each row, the number of leading spaces is n - row_index, and the number of stars is 2 * row_index - 1.
I first build the upper half by increasing the row_index, then the lower half by decreasing it.
The time complexity is O(n^2) because the total number of printed characters grows quadratically with n, and this cannot be optimized since every star must be printed.
"""

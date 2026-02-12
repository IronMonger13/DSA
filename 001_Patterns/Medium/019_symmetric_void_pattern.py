"""
INTUITION:
Print symmetric pattern, which is a combination of 4 triangles, forming an empty diamond shape in between. So stars first decrease from n to 1, and then increase back from 1 to n.


APPROACH:
Run a loop from n to 1 for row control for top half of the pattern, and loop from 1 to n for row control for bottom half of the pattern.
Inside both loops:
1. Count number of spaces as (n - current row number) * 2 to keep left triangles left aligned and right triangles right aligned.
2. Print current row number of stars, then print " " * spaces, and then print current row number of stars again.


EDGE CASES:
n = 0 - nothing is printed.
"""


# CODE SOLUTION:
def symmetric_void_pattern(n):
    for row in range(n, 0, -1):
        spaces = (n - row) * 2
        print("*" * row + " " * spaces + "*" * row)

    for row in range(1, n + 1):
        spaces = (n - row) * 2
        print("*" * row + " " * spaces + "*" * row)


symmetric_void_pattern(5)


"""
TIME COMPLEXITY:
O(n^2) since output size grows quadratically with n.


SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force is optimal approach since all stars need to be printed.


WHAT I'D SAY IN AN INTERVIEW:
We have to print a pattern which consists of 4 triangles, when put together forms a blank diamond in between.
Run two loops, first for top half of pattern and second for bottom half of the pattern. Inside each loop count number of spaces required to keep left triangles left aligned and right triangles right aligned. Print current row number of stars, followed by spaces of " " and again current row number of stars in the same row for each row.
Time complexity of O(n^2) is optimal since all stars need to be printed, so output size grows quadratically with n.
"""

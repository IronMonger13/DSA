"""
INTUITION:
Print a hollow rectangle for n rows and n columns, as if printing the boundary of a square/rectangle.


APPROACH:
Run a loop from 1 to n for row control.
Check if the current row number is 1 or n. If true, print n number of stars. If false, run a loop from 1 to n and check if current column number is 1 or n. If true, print 1 star. If false, print a space.


EDGE CASES:
n = 0 - nothing is printed.
"""


# CODE SOLUTION:
def hollow_rectangle_pattern(n):
    for row in range(1, n + 1):
        if row == 1 or row == n:
            print("*" * n, end="")
        else:
            for col in range(1, n + 1):
                if col == 1 or col == n:
                    print("*", end="")
                else:
                    print(" ", end="")
        print()


hollow_rectangle_pattern(5)

"""
TIME COMPLEXITY:
O(n^2) since output size grows quadratically with n.

SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force is optimal since all stars need to be printed.


WHAT I'D SAY IN AN INTERVIEW:
We have to print a hollow square of n rows and n columns.
We run a loop, and check if current row or column number is 1 or n. If it is, we print a star else we print a space.
Time complexity of O(n^2) is optimal since all stars need to be printed, so output size grows quadratically with n.
"""

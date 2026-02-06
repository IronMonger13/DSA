"""
INTUITION:
A right-angled triangle pattern grows row by row.
The first row contains one star, the second row contains two stars, and in general, the i-th row contains i stars.


APPROACH:
In each iteration, print '*' repeated i times to form the current row.


EDGE CASES:
n = 0 - nothing is printed.
"""


# CODE SOLUTION:
def right_angles_triangle_pattern(n):
    for i in range(1, n + 1):
        print("*" * i)


right_angles_triangle_pattern(1)


"""
TIME COMPLEXITY:
O(n^2) since the total number of printed characters grows on the order of n^2.


SPACE COMPLEXITY:
O(1) since no additinal data structure was used.


WHY BRUTE FORCE FAILS:
There is no shortcut to avoid printing the stars.
Since the total number of stars printed is 1 + 2 + ... + n, every character must be output.
This enforces the time complexity regardless of the implementation.


WHAT I'D SAY IN AN INTERVIEW:
Each row contains as many stars as its row number.
By looping from 1 to N and printing i stars per row, we directly construct the pattern.
The time complexity is unavoidable because all stars must be printed.
"""

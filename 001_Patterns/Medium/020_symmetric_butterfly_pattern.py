"""
INTUITION:
Print a pattern that combines 4 right angled triangles in such a way that the pattern appears to be a symmetric butterfly. The number of stars increase from first row till n, then decrease till the first row.


APPROACH:
Divide the pattern into two halves horizontally.
First run a loop for row control of upper half from 1 to n, and second loop for row control of lower half from n - 1 to 1.
Inside each loop, count number of spaces as (n - current row number) * 2, to keep the left triangle left aligned and right triangle right aligned, keeping the spacing in the pattern preserved. Then print star current row number of times, followed by the " " spaces number of times, and end with star printed current row number of times again.


EDGE CASES:
n = 0 - nothing is printed.
"""


# CODE SOLUTION:
def symmetric_butterfly_pattern(n):
    for row in range(1, n + 1):
        spaces = 2 * (n - row)
        print("*" * row + " " * spaces + "*" * row)

    for row in range(n - 1, 0, -1):
        spaces = 2 * (n - row)
        print("*" * row + " " * spaces + "*" * row)


symmetric_butterfly_pattern(5)


"""
TIME COMPLEXITY:
O(n^2) since output size grows quadratically with n.


SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force is optimal since all stars need to be printed.


WHAT I'D SAY IN AN INTERVIEW:
We have to print 4 triangles arranged in such a way that their combination looks like a symmetric butterfly. 
We run 2 loops, one for upper half of the pattern and one for lower half of the pattern, and for each loop, we calculate number of spaces required to maintain the shape of the pattern, then print stars on both sides for each row with spaces in between to print the pattern.
Time complexity of O(n^2) is optimal since output size grows quadratically with n as all stars need to be printed.
"""

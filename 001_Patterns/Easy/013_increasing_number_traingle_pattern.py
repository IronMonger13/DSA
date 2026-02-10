"""
INTUITION:
A right angles triangle where all values print in increasing order by 1 globally.


APPROACH:
Initialise a variable (num) to 1
Run a loop from 1 to n for row control.
For each row iteration, run a loop from 1 to current row number.
Print num and increment by 1.
Add new line after each row iteration.


EDGE CASES:
n = 0 - nothing is printed.
"""


# CODE SOLUTION:
def increasing_number_triangle_pattern(n):
    num = 1
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print(num, end=" ")
            num += 1
        print()


increasing_number_triangle_pattern(5)

"""
TIME COMPLEXITY:
O(n^2) since output size grows quadratically with n.


SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force is acceptable since all numbers need to be printed.

WHAT I'D SAY IN AN INTERVIEW:
We have to print a right angled triangle for n rows where each value increases by 1 globally.
We loop from 1 to n, then run inner loop from 1 to current row number, then print the number and increment it by 1.
O(n^2) since all numbers need to be printed, so it is optimal time complexity.
"""

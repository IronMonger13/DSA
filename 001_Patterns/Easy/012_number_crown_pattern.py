"""
INTUITION:
We have to print number crown pattern, where each row contains numbers in increasing order starting from 1 to current, followed by spaces, and then in decreasing order from current row to 1.


APPROACH:
Run a loop from 1 to n for row control.
For each row, run a loop from 1 to row number to print the increasing numbers.
Then run a loop for spaces to print 2*(n-row) spaces. This is because we need to print 2 spaces for each missing number in the row.
Then run a loop from row number to 1 to print the decreasing numbers.

EDGE CASES:
n = 0 - nothing is printed.
"""


# CODE SOLUTION:
def number_crown_pattern(n):
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print(col, end="")
        for space in range(n - row):
            print(" " * 2, end="")
        for col in range(row, 0, -1):
            print(col, end="")
        print()


number_crown_pattern(5)


"""
TIME COMPLEXITY:
O(n^2) since output size grows quadratically with n.


SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force is optimal since we have to print all the numbers in the pattern.


WHAT I'D SAY IN AN INTERVIEW:
Explain in 3 points:
The problem is to print a number crown pattern where each row contains number in increasing order from 1 to current row number, followed by spaces and then numbers in decreasing order from current row number to 1.
We do so by looping through each row and printing the required numbers and spaces.
O(n^2) is optimal since all numbers in the pattern need to be printed.
"""

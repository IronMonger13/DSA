"""
INTUITION:
We have to print a pyramid pattern for n rows where for each row, character value first increases from A to current row number, then decreases back to A.


APPROACH:
Run a loop from 1 to n for row control.
For each row:
1. Initialise a character variable (char) to A.
2. Calculate number of spaces as (n - current row number) * 2, and print " " * spaces.
3. Run first inner loop from 1 to current row number and print required characters in increasing order from A.
4. Decrease current char value by 1 which was increased by 1 at the end of the first loop.
5. Run second inner loop from current row number to 2 to print characters in decreasing order till A.


EDGE CASES:
n = 0 - nothing is printed.
"""


# CODE SOLUTION:
def alpha_hill_pattern(n):
    for row in range(1, n + 1):
        char = "A"
        spaces = (n - row) * 2
        print(" " * spaces, end="")
        for col in range(1, row + 1):
            print(char + " ", end="")
            char = chr(ord(char) + 1)
        char = chr(ord(char) - 1)
        for col in range(row, 1, -1):
            char = chr(ord(char) - 1)
            print(char + " ", end="")
        print()


alpha_hill_pattern(3)


"""
TIME COMPLEXITY:
O(n^2) since output size grows quadratically with n.


SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force is optimal since all characters need to be printed.


WHAT I'D SAY IN AN INTERVIEW:
We have to print a pyramid pattern where all characters are centre aligned and in increasing order from A till current row number and then decrease back till A.
We run an outer loop for row control, and then count number of spaces to be printed to keep the characters center aligned. Then we run first inner loop to print characters in increasing order, and second loop in decreasing order. Between both loops, we decrement the value of char by 1 to compensate for the extra increment at the end of first loop.
Time complexity of O(n^2) is optimal since all characters need to be printed, so output size grows quadratically with n.
"""

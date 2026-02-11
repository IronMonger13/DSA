"""
INTUITION:
Print a triangle pattern for n rows where character to be printed and number of times it has to be printed increases with the current row number, starting from A.


APPROACH:
Initialise a character variable (char) to A.
Run a loop from 1 to n for row control.
For each row:
1. Run an inner loop from 1 to current row number
2. Print char.
After each row iteration, increment char by converting it to its ASCII code, increment by 1, and convert it back to character data type.


EDGE CASES:
n = 0 - nothing is printed.
"""


# CODE SOLUTION:
def alpha_ramp_pattern(n):
    char = "A"
    for row in range(1, n + 1):
        for col in range(0, row):
            print(char, end="")
        char = chr(ord(char) + 1)
        print()


alpha_ramp_pattern(5)


"""
TIME COMPLEXITY:
O(n^2) since output size grows quadratically with n.


SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force is optimal since all characters need to be printed.


WHAT I'D SAY IN AN INTERVIEW:
We have to print a triangle pattern in which character value increases with each row, and each row prints the character current row number of times, starting with A.
We initialise a character to A, then run a loop from 1 to n to control rows. For each row, we print the character the current row number of times, and after each row iteration, we increment the character value by 1.
Time complexity of O(n^2) is optimal since all the characters need to be printed, so the output size grows quadratically with n.
"""

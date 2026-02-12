"""
INTUITION:
Print a right angled triangle where as number of rows increase, number of characters to be printed increases and starting character decreases in value per row, and it increases per column in value.


APPROACH:
Run a loop from 0 to n - 1 for row control.
Initialise character variable (char) to current row value as ASCII code for 'A' + n - 1 - current row number.
For each row, print character and increase its value by 1.


EDGE CASES:
n = 0 - nothing is printed.
"""


# CODE SOLUTION:
def alpha_triangle_pattern(n):
    for row in range(0, n):
        char = ord("A") + n - 1 - row
        for col in range(0, row + 1):
            print(chr(char) + " ", end="")
            char += 1
        print()


alpha_triangle_pattern(3)


"""
TIME COMPLEXITY:
O(n^2) since output size grows quadratically with n.


SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force is efficient since all characters need to be printed, so output size grows quadratically with n.


WHAT I'D SAY IN AN INTERVIEW:
We have to print a right angled triangle where each row starts with character as 'A' + n - 1 - current row number, and increase it by 1 per column iteration. The starting character's value decreases by 1 with each row iteration.
We start by running a loop for row control. Inside each row we first initialise the character as stated, and then increment its value by 1 with each column iteration.
Time complexity of O(n^2) is optimal since all characters need to be printed, so the output size grows quadratically with n.
"""

"""
INTUITION:
Print a right angled triangle where each character increases by 1 within each row, and resets back to 'A' after each row.


APPROACH:
Run a loop from 1 to n for row control.
Initialise a variable (char) to 'A'.
For each row, going from 1 to current row number:
1. Print char.
2. Increment its value by 1 by first converting char into its integer ASCII value and then converting it back into char.


EDGE CASES:
n = 0 - nothing is printed.
"""


# CODE SOLUTION:
def increasing_letter_triangle_pattern(n):
    for row in range(0, n):
        char = "A"
        for col in range(0, row + 1):
            print(char, end="")
            char = chr(ord(char) + 1)
        print()


increasing_letter_triangle_pattern(5)


"""
TIME COMPLEXITY:
O(n^2) since output size grows quadratically with n.


SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force is optimal since all characters need to be printed.


WHAT I'D SAY IN AN INTERVIEW:
We have to print a right angled triangle where each row starts with character A, and prints till the current row number.
We loop till n, and in each iteration, print characters till current row number. To increment character value, we convert them into their integer ASCII value and increment that by 1, and again convert it back to character.
Time complexity of O(n^2) is optimal since all characters need to be printed.
"""

"""
INTUITION:
Print an inverted triangle for n rows where each row has characters going from A to current row number.


APPROACH:
Run a loop from n to 1 for row control.
Initialise a character (char) to A.
For each row:
1. Run an increasing loop till current row number.
2. Print the character in the same line.
3. Convert char to its ASCII code and increment it by 1, and convert it back into character data type.


EDGE CASES:
n = 0 - nothing is printed.
"""


# CODE SOLUTION:
def reverse_letter_triangle_pattern(n):
    for row in range(n, 0, -1):
        char = "A"
        for col in range(0, row):
            print(char, end="")
            char = chr(ord(char) + 1)
        print()


reverse_letter_triangle_pattern(3)


"""
TIME COMPLEXITY:
O(n^2) since output size grows quadratically with n.


SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force is optimal approach since all characters need to be printed.


WHAT I'D SAY IN AN INTERVIEW:
We have to print an inverted triangle where each row has characters going from 'A' to the current row number.
We run a loop from n to 1, and inside each row we print characters in increasing order, and increment character value by 1 by first converting it to its ASCII, increment by 1, and then converting it back to character data type.
Time complexity of O(n^2) is optimal since all values need to be printed, for which the output size grows quadratically with n.
"""

"""
INTUITION:
This is an inverted right-angled number triangle.
The first row prints numbers from 1 to n.
Each next row prints one less number, until it reaches 1.


APPROACH:
Run a loop from n down to 1 to control the rows.
For each row, run another loop from 1 up to the current row number.
Print the numbers in increasing order on the same line.
Move to a new line after finishing each row.


EDGE CASES:
n = 0 - nothing is printed.
"""


# CODE SOLUTION:
def inverted_numbered_right_pyramid(n):
    for row in range(n, 0, -1):
        for col in range(1, row + 1):
            print(col, end="")
        print()


inverted_numbered_right_pyramid(6)


"""
TIME COMPLEXITY:
O(n^2) because the total count of printed numbers grows with n.


SPACE COMPLEXITY:
O(1) since no additonal data structures were used.


WHY BRUTE FORCE FAILS:
Every number that appears in the output must be printed, so the work cannot be reduced.


WHAT I'D SAY IN AN INTERVIEW:
Each row prints numbers from 1 up to its row index, starting from n and decreasing.
Since all numbers must be printed, the time complexity is unavoidable.
"""

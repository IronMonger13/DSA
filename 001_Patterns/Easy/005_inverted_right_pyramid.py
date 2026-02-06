# CODE SOLUTION:
def inverted_right_pyramid(n):
    for i in range(n, 0, -1):
        print("*" * i)


inverted_right_pyramid(0)


"""
INTUITION:
This is a right-angled pyramid printed in reverse.
The first row has n stars, and each next row has one star less, going down to 1.


WHY BRUTE FORCE FAILS:
Every star that appears in the output must be printed, so the amount of work cannot be reduced or skipped.


APPROACH:
Run a loop from n down to 1.
In each iteration, print '*' repeated i times to form the current row.


TIME COMPLEXITY:
O(n^2) because the total number of stars printed grows with n.


SPACE COMPLEXITY:
O(1) since no additional data structure was used


EDGE CASES:
n = 0 - nothing is printed


WHAT I'D SAY IN AN INTERVIEW:
Each row prints the same number of stars as its row index, starting from n and decreasing.
Since all stars must be printed, the time complexity is unavoidable.
"""

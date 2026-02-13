"""
INTUITION:
Print a square matrix where each number is n - its distance from the matrix's boundary. The outermost boundary has value of n, which decreases as we keep getting inside, going till 1 in the centre.


APPROACH:
Run an inner and outer loop from 0 to 2n - 2 for row and column control respectively.
For each number in the matrix, calculate its distance from the boundary of the matrix.
Each number will be n - minimum distance from the boundary.


EDGE CASES:
n = 0 - nothing is printed.
"""


# CODE SOLUTION:
def the_number_pattern(n):
    for row in range(0, 2 * n - 1):
        for col in range(0, 2 * n - 1):
            top = row
            bottom = 2 * n - 2 - row
            left = col
            right = 2 * n - 2 - col
            print(n - min(top, bottom, left, right), end="")
        print()


the_number_pattern(4)


"""
TIME COMPLEXITY:
O(n^2) since output size grows quadratically with n.


SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force is optimal since all numbers need to be printed.


WHAT I'D SAY IN AN INTERVIEW:
We have to print square matrix of 2n-1 rows and columns where each number is n - minimum distance from the boundary of the matrix.
Run two nested loops from 0 to 2n-2 for row and column control. Find out the minimum distance from the matrix's boundary, and print n - minimum distance to get the final matrix pattern.
Time complexity of O(n^2) is optimal since output size grows quadratically with n as all numbers need to be printed.
"""

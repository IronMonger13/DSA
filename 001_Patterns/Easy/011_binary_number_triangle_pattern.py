"""
INTUITION:
print right angled triangle for n rows where each row prints 1 and 0 alternatively, starting with 1 on odd rows and 0 on even rows.


APPROACH:
Run a loop from 1 to n.
For each row, check its index:
- If row index is odd, set num to 1.
- If row index is even, set num to 0.
In each row iteration, print starting value once per row (num), and then alternate between each print within row.


EDGE CASES:
n = 0 - nothing is printed.
"""


# CODE SOLUTION:
def binary_number_triangle_pattern(n):
    for row in range(1, n + 1):
        if row % 2 != 0:
            num = 1
        else:
            num = 0

        for col in range(1, row + 1):
            print(num, end=" ")
            if num == 0:
                num = 1
            else:
                num = 0
        print()


binary_number_triangle_pattern(3)


"""
TIME COMPLEXITY:
O(n^2) since numbers to be printed grow quadratically with n.


SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force is optimal since all the numbers need to be printed.


WHAT I'D SAY IN AN INTERVIEW:
This pattern prints a right-angled triangle of binary values.
Each row starts with a fixed value: odd rows start with 1 and even rows start with 0.
Within a row, the value alternates between 1 and 0 after each print.
Time complexity of O(n^2) is optimal because output size grows with n.
"""

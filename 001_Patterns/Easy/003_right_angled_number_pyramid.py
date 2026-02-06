"""
INTUITION:
The pattern consists of N rows.
In the i-th row, numbers are printed sequentially from 1 up to i.
Each row therefore grows by one number compared to the previous row.


APPROACH:
Run an outer loop from 1 to N to control the rows.
For each row i, run an inner loop from 1 to i and print the numbers sequentially.
Print a newline after completing each row.


EDGE CASES:
n = 0 - nothing is printed.
"""


# CODE SOLUTION:
def right_angled_number_pyramid(n):
    for rows in range(1, n + 1):
        for cols in range(1, rows + 1):
            print(cols, end="")
        print()


right_angled_number_pyramid(3)


"""
TIME COMPLEXITY:
O(n^2) since the total number of printed values grows on the order of n^2.


SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
There is no way to avoid printing every number in the pattern.
Since the total count of printed numbers grows as 1 + 2 + ... + N, the required work is inherent to the output itself.


WHAT I'D SAY IN AN INTERVIEW:
Each row prints numbers from 1 up to its row index.
By nesting a loop that runs up to the current row inside a loop from 1 to N, we can directly generate the required number pyramid.
The time complexity is unavoidable because all numbers must be printed.
"""

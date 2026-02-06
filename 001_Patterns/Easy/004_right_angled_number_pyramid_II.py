"""
INTUITION:
For the i-th row, the number i is printed i times.
So each row simply repeats its row number.


APPROACH:
Run a loop from 1 to n.
For each value of i, convert it to a string and print it i times.


EDGE CASES:
n = 0 - nothing is printed.
"""


# CODE SOLUTION:
def right_angled_number_pyramid_II(n):
    for i in range(1, n + 1):
        print(str(i) * i)


right_angled_number_pyramid_II(6)


"""
TIME COMPLEXITY:
O(n^2) because the total number of printed characters increases as n grows.


SPACE COMPLEXITY:
O(1) since no additonal data strucutre was used.


WHY BRUTE FORCE FAILS:
All numbers shown in the output must be printed, so the amount of work cannot be reduced.


WHAT I'D SAY IN AN INTERVIEW:
Each row prints its row number repeatedly.
Since every value in the output must be printed, the time complexity is unavoidable.
"""

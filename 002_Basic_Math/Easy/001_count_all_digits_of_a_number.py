"""
INTUITION:
For a given number n, count the number of digits it has.


APPROACH:
If n is negative, we convert it to its absolute value, and if n is 0, we print 1.
Take log 10 of number, convert it to integer, and add 1 to the final result to keep the output correct, since log10(n) gives n-1 digits.


EDGE CASES:
n = 0 - 1 is printed
"""

# CODE SOLUTION:
import math


def count_all_digits_of_a_number(n):
    if n < 0:
        n = abs(n)
    if n == 0:
        print(1)
        return None

    count = int(math.log10(n)) + 1
    print(count)


count_all_digits_of_a_number(0)


"""
TIME COMPLEXITY:
O(1) since we only have to perform 1 logarithmic operation.


SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force involves repeatedly dividing the number by 10 till we get 0, which involves log10(n) number of operations. This approach is optimal since we perform a logarithmic operation only once, which takes only O(1) time.


WHAT I'D SAY IN AN INTERVIEW:
We have to find out the number of digits in a given number.
We use log of base 10 which gives us the number of digits in the number in O(1) time, and add 1 to the result to get the correct output. If n is negative, we take absolute value of the number. If n is 0, we print 1.
Time and space complexity are O(1) which are both optimal.
"""

"""
INTUITION:
Find greatest common divisor of 2 numbers.


APPROACH:
Keep taking modulo of n1 with n2 as divisor, and swap n1 and n2 values with each other after each iteration.
Repeat this until n2 is 0. Once we reach 0 on n2, n1 is the greatest common divisor.


EDGE CASES:
n1 or n2 = 0 - return other number
n1 or n2 = 1 - return 1
"""


# CODE SOLUTION:
def gcd_of_two_numbers(n1, n2):
    n1 = abs(n1)
    n2 = abs(n2)

    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    if n1 == 1 or n2 == 1:
        return 1

    while n2 != 0:
        n1, n2 = n2, n1 % n2

    return n1


print(gcd_of_two_numbers(20, -15))


"""
TIME COMPLEXITY:
O(log n) since we number of steps taken are only the number of times we perform the modulo operation till either n1 reaches 0, which takes log n time.


SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force fails because we start from 1 till the smaller number in n1 and n2, and we keep checking for each value if both numbers are divisible, which takes O(n) time.


WHAT I'D SAY IN AN INTERVIEW:
We have to find the greatest common divisor of the 2 given numbers.
First we take absolute values of the 2 given numbers. Then we keep taking modulo of n1 using n2 as divisor and swap n1 and n2 values in each iteration till we reach 0 on n2. After this, n1 is the greatest common divisor. This is called Euclidean's algorithm. If either number is 0, we early return the other number, and if either numbers is 1, we early return 1.
Time complexity is O(log n), which is optimal since we only iterate the number of times as we are performing the modulo operation till we get 0 for either number, which takes log n number of iterations. Space complexity is O(1) since no additional data structures were used.
"""

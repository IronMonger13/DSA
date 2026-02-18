"""
INTUITION:
Recursively find out the sum of first n numbers starting from 1.


APPROACH:
Define a function that takes n as parameter.
Define base case: return when n <= 0.
Recursively call the function passing n-1 as parameter.
When going back up from the recursive stack, add the numbers formulated in each recursive call.


EDGE CASES:
n <= 0 - return 0
"""


# CODE SOLUTION:
def sum_of_n(n):
    if n <= 0:
        return 0

    return n + sum_of_n(n - 1)


print(sum_of_n(5))


"""
TIME COMPLEXITY:
O(n) since we have to perform n number of operations.


SPACE COMPLEXITY:
O(n) since stack space was used for recursive calls.


WHY BRUTE FORCE FAILS:
A direct formula can compute the result in O(1) time and O(1) space, but since the problem requires recursion, this is the optimal recursive approach.


WHAT I'D SAY IN AN INTERVIEW:
We have to recursively add numbers from 1 to n to find out the sum of first n numbers.
The function would be f(n) = n + f(n -1), where f(0) = 0. We first define a function that takes n as parameter. Then define our base case when n <= 0, return 0. This will also handle edge cases. Then we simply return n + function with n - 1 as parameters. Each call waits for the result of sum_of_n(n-1), then adds n to it.
Time complexity is O(n) since we have to perform n number of operations. Space complexity is O(n) since stack space was used for recursive calls.
"""

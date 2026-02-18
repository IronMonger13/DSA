"""
INTUITION:
Recursively find out the factorial of a given number.


APPROACH:
Finding factorial follows this expression: f(n) = n * f(n - 1), f(1) = 1.
Define a function that takes n as parameter.
Define base case: if n <= 1 - return 1.
Return n * fun(n - 1). This way each recursive call with wait for n - 1 to resolve first, and then multiply it to n to get the factorial.


EDGE CASES:
n <= 1 - return 1
"""


# CODE SOLUTION:
def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))


"""
TIME COMPLEXITY:
O(n) since we have to perform n operations.


SPACE COMPLEXITY:
O(n) since stack space was used for recursive calls.


WHY BRUTE FORCE FAILS:
Iterative approach is optimal for this as it takes O(1) space but since we had to solve specifically using recursion, this is the optimal approach.


WHAT I'D SAY IN AN INTERVIEW:
We have to recursively find out the factorial of n numbers.
We follow this expression - f(n) = n * f(n - 1) where f(1) = 1.
We first define the function that takes n as parameter. Then we define the base case as return 1 when n <= 1. This also handles the edge cases. Then we multiply n with a recursive call for function with n-1 as parameter. So each function call waits for the resolution of f(n-1) and multiplies it with n to get the factorial.
Time complexity is O(n) since we need to perform n number of operations. Space complexity is O(n) since stack space is used for recursive calls.
"""

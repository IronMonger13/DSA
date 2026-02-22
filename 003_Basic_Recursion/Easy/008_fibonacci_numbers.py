"""
INTUITION:
Recursively print the fibonacci value for n. Fibonacci number is sum of previous two fibonacci numbers starting from F(0) = 0, F(1) = 1, F(2) = F(0) + F(1) = 0 + 1 = 1 and so on.

APPROACH:
Define base case: return when n <= 1.
Define a function that takes n as parameter.
Recursively call F(n-1) and F(n-2) and add these two to get F(n).


EDGE CASES:
n = 0 - return 0
n = 1 - return 1
"""


# CODE SOLUTION:
class Solution:
    def fib(n: int) -> int:
        if n <= 1:
            return n

        return Solution.fib(n - 1) + Solution.fib(n - 2)


print(Solution.fib(4))


"""
TIME COMPLEXITY:
O(2^n) - each recursion call can have 2 more recursion calls in the worst case, so we have to perform 2^n operations.


SPACE COMPLEXITY:
O(n) - additional stack space is used for recursive calls.


WHY BRUTE FORCE FAILS:
Any approach using recursion will take O(2^n) time and O(n) space so this approach is acceptable.


WHAT I'D SAY IN AN INTERVIEW:
We have to recursively find out the fibonacci value for n.
We first define a function that takes n as parameter. Then we define our base case as return n when n<=1. Then we recursively call functions as function(n-1) + function(n-2). This will recursively find out the sum of f(n-1) and f(n-2), and ultimately return the fibonacci number for n.
Time complexity is O(2^n) since each recursive call will have 2 more recursive calls in the worst case. Space complexity is O(n) since additional stack space is used for recursive calls
"""

"""
INTUITION:
Recursively print from n to 1.


APPROACH:
Define a function that takes n as parameter.
Define base case: return when n <= 0.
Print n.
Recursively call the function passing n - 1 as parameter.


EDGE CASES:
None
"""


# CODE SOLUTION:
def n_to_1(n):
    if n <= 0:
        return

    print(n)

    n_to_1(n - 1)


n_to_1(5)


"""
TIME COMPLEXITY:
O(n) since number of operations have to be performed.


SPACE COMPLEXITY:
O(n) since stack space is used for recursive stack.


WHY BRUTE FORCE FAILS:
Brute force is the only way of solving this problem. n number of operations have to be performed.


WHAT I'D SAY IN AN INTERVIEW:
We have to print from n to 1 recursively.
We define a function that takes n as parameter. Then we define our base case that if n is less than or equal to 0 we return, and then print n. Then we recursively call the function passing n - 1 as parameter.
Time complexity is O(n) since n number of operations have to be performed, and space complexity is O(n) since stack space is required for recursive calls.
"""

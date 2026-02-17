"""
INTUITION:
Recursively print from 1 to n.


APPROACH:
Define a function with starting count and n as parameters, and set count to 1 by default.
Define base case: return when count > n.
Print count.
Recursively call the function passing count+1 and n as parameters.


EDGE CASES:
None
"""


# CODE SOLUTION:
def one_to_n(n, count=1):
    if count > n:
        return

    print(count)

    one_to_n(n, count + 1)


one_to_n(5)


"""
TIME COMPLEXITY:
O(n) since we have to perform n number of operations.


SPACE COMPLEXITY:
O(n) since stack space is used for recursive stack.


WHY BRUTE FORCE FAILS:
Brute force is optimal since we need to perform n operations.


WHAT I'D SAY IN AN INTERVIEW:
We have to print from 1 to n using recursion.
We define the function taking n and starting count as parameters and setting default value for n to 1. Then we add our base case: return when count > n. Print the count, and recursively call the function passing n and count + 1 as parameters.
Time complexity is O(n) since we have to perform n number of operations, and space complexity is O(n) since stack space was used for recursive calls.
"""

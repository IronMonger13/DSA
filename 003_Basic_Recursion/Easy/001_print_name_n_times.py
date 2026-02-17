"""
INTUITION:
Use recursion to print name n number of times.


APPROACH:
Define a function that takes starting count, n and name as parameter.
If count = n, terminate the function.
Print name.
Recursively call the function, passing starting count + 1, n and name as the parameters.


EDGE CASES:
None
"""


# CODE SOLUTION:
def print_name(count, n, name):
    if count == n:
        return

    print(name + " ", end="")

    print_name(count + 1, n, name)


print_name(0, 5, "ABC")


"""
TIME COMPLEXITY:
O(n) since we perform n number of operations.


SPACE COMPLEXITY:
O(n) since stack space was used for recursive stack.


WHY BRUTE FORCE FAILS:
Brute force is optimal since we have to perform n number of operations.


WHAT I'D SAY IN AN INTERVIEW:
We have to print name n number of times using recursion.
We first add our base case to define when to terminate the functions calling itself recursively. We accept starting count, n and name in parameters, and add our base case of when count == n, we terminate. Then we print name and recursively call the function, passing the count + 1, along with n and name.
Time complexity is O(n) since we have to print name n number of times, and space complexity is O(n) since stack space was used for recursive calls.
"""

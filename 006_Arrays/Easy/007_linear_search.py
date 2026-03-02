"""
INTUITION:
Given an array oif length n and a number num, return index of num in arr, if not found return -1. Solve using linear search.


APPROACH:
1. Run a loop from 0 to n-1.
2. For each iteration, check if the element is equal to num.
3. If equal, return the index.
4. Return -1 if all iterations are over.


EDGE CASES:
n = 0 - return -1 as array has no elements.
"""


# CODE SOLUTION:
def linear_search(arr, num):
    n = len(arr)

    for i in range(0, n):
        if arr[i] == num:
            return i

    return -1


arr = [1, 2, 3, 4, 5]
num = 1
print(linear_search(arr, num))


"""
TIME COMPLEXITY:
O(n) - we traverse the array once to find the given number, which takes O(n) time.


SPACE COMPLEXITY:
O(1) - no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force works here because linear search will always take O(n) time and O(1) space for any given inputs.


WHAT I'D SAY IN AN INTERVIEW:
We have to use linear search to find out if num exists in arr or not.
We iterate through the entire array, and for each element, we compare if the current element is equal to num or not. If equal, we return the index, else after all iterations are complete, we return -1. We early return -1 if array's length is 0, meaning the array has no elements.
Time complexity is O(n) since we iterate through the array once to find num. Space complexity is O(1) since no additional data structures were used.
"""

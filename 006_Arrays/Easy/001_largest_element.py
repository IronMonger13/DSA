"""
INTUITION:
Given an array of size n, find the largest element.


APPROACH:
Initialise a pointer at the first element of the array.
Iterate through the array, and for each element, compare it with the pointer. If element > largest, move the pointer to the element.
Once the array has been iterated through, return the element at pointer's index.


EDGE CASES:
n = 0 - return None.
"""


# CODE SOLUTION:
def largest_element(arr):
    if len(arr) == 0:
        return None

    largest = arr[0]

    for element in arr:
        if element > largest:
            largest = element

    return largest


arr = [8, 10, 5, 7, 9]
print(largest_element(arr))


"""
TIME COMPLEXITY:
O(n) - we have to iterate through the array only once, which takes O(n) time.


SPACE COMPLEXITY:
O(1) - no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force is inefficient since it involves comparing each element with all the other elements to check if it the largest or not, which takes O(n^2) time. This approach is optimal since we only have to iterate through the array once and by moving the pointer after comparisons, we get the largest element in O(n) time.


WHAT I'D SAY IN AN INTERVIEW:
We have to find the largest element in a given array.
We set a pointer at the first element, and compare each element with the pointer as we iterate through the array. If for any element we get element > pointer, we move pointer to that element. After all iterations are complete, the pointer has the largest element.
Time complexity is O(n) since we only iterate through the array once, and space complexity is O(1) since no additional data structures were used.
"""

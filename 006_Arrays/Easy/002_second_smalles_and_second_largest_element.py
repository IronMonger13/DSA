"""
INTUITION:
For a given array, find out the second largest and second smallest elements.


APPROACH:
Initialise 4 variables - largest, second_largest, smallest, and second_smallest.
Set largest and second_largest to -inf, and smallest and second_smallest to +inf.
Iterate through the array, and for each element:
1. Check if element > largest, if true, then second_largest = largest and largest = element. If not, check if element > second_largest and element != largest, if true, set second_largest = element.
2. Check if element < smallest, if true, second_smallest = smallest and smallest = element. If not, check if element < second_smallest and element != smallest, if true, set second_smallest = element.
Once iterated through the entire array, return an array as [second_smallest, second_largest].
If second largest or second smallest is still inf, that means second largest could not be found and elements are duplicate, so return [-1, -1].


EDGE CASES:
len(arr) < 2 - return -1.
"""

# CODE SOLUTION:
import math


def second_smallest_and_second_largest(arr):
    if len(arr) < 2:
        return [-1, -1]

    largest = 0 - math.inf
    second_largest = 0 - math.inf

    smallest = math.inf
    second_smallest = math.inf

    for element in arr:
        if element > largest:
            second_largest = largest
            largest = element
        elif element > second_largest and element != largest:
            second_largest = element

        if element < smallest:
            second_smallest = smallest
            smallest = element
        elif element < second_smallest and element != smallest:
            second_smallest = element

    if second_smallest == math.inf or second_largest == -math.inf:
        return [-1, -1]

    return [second_smallest, second_largest]


arr = [7, 7, 7]
print(second_smallest_and_second_largest(arr))


"""
TIME COMPLEXITY:
O(n) - we only iterate through the array once.


SPACE COMPLEXITY:
O(1) - no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force is inefficient as it involves sorting the array in ascending order and then picking element on index 1 as second smallest and element on len(arr) - 2 as second largest index, but even the most optimal sorting algorithm takes O(n log n) time and O(log n) space. This approach is optimal since we are able to find the second smallest and second largest just by using variables to store largest and second largest, and similarly for smallest and second smallest, and by iterating through the array once, which takes O(n) time and O(1) space.


WHAT I'D SAY IN AN INTERVIEW:
We have to find the second largest and second smallest element in the given array, and return -1 if not possible.
We first check if length of array is less than 2, that means second smallest and second largest cannot exist, so we return -1. We define 4 variables to keep track of largest, second largest, smallest and second smallest elements. For each element, we check if element is greater than largest, if it is, we update second largest as largest and largest as the element. If not, we check if element is greater than the second largest and not greater than largest, if true, we update second largest as element. Similarly, we can find out the smallest and second smallest. We finally return an array of second smallest and second largest.
Time complexity is O(n) since we only have to traverse the array once. Space complexity is O(1) since no additional data structures were used.
"""

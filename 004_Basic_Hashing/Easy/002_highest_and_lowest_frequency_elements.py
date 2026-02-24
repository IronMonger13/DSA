"""
INTUITION:
Given an array, return the highest and lowest occurring elements.


APPROACH:
Iterate through the array and store the frequencies in a hashmap.
Return key for maximum value and minimum value.


EDGE CASES:
len(arr) = 0 - return None
"""

# CODE SOLUTION:
from collections import defaultdict


def highest_and_lowest_frequency_elements(arr):
    if len(arr) == 0:
        return None

    mpp = defaultdict(int)

    for i in arr:
        mpp[i] += 1

    max_element = None
    max_frequency = 0
    min_element = None
    min_frequency = len(arr)

    for key, value in mpp.items():
        if value > max_frequency:
            max_frequency = value
            max_element = key

        if value < min_frequency:
            min_frequency = value
            min_element = key

    return [max_element, min_element]


arr = [2, 2, 3, 4, 4, 2]
print(highest_and_lowest_frequency_elements(arr))


"""
TIME COMPLEXITY:
O(n) - since we iterate through the array only once to store all elements in hashmap, which takes O(n) time and then through the hashmap, which takes O(k) time. So total time taken is O(n + k), which simplifies to O(n).


SPACE COMPLEXITY:
O(n) - since additional space is used for hashmap.


WHY BRUTE FORCE FAILS:
Brute force is inefficient since for each element, we iterate the array again to check for its counts, making all operations to perform in O(n^2) time. This approach is optimal since we iterate through the array only once and store all elements and their frequencies in hashmap, which takes O(n) time.


WHAT I'D SAY IN AN INTERVIEW:
We have to find the highest and lowest occurring elements in a given array.
We iterate through the array to store all the unique elements and their frequencies in a hashmap. Then we iterate through the hashmap to find out the maximum and minimum keys as result. We return None when array is empty.
Time complexity is O(n) since we only need to iterate through the array once to store all unique elements and their frequencies in hashmap, which takes O(n) time, and then once through hashmap, which takes O(k) time. So total time taken is O(n + k), which simplifies to O(n). Space complexity is O(n) since additional space is used for hashmap.
"""

"""
INTUITION:
Count the frequencies of all elements in the array.

APPROACH:
Create a hashmap to store the elements and their frequencies in key value pairs.
Iterate through the array and store the elements as keys, and increment value count by 1 for each element.


EDGE CASES:
n = 0 - empty hashmap is returned.
"""

# CODE SOLUTION:
from collections import defaultdict


def count_frequency(arr):
    mpp = defaultdict(int)

    for i in arr:
        mpp[i] += 1

    return mpp.items()


arr = [2, 2, 3, 4, 4, 2]
print(count_frequency(arr))


"""
TIME COMPLEXITY:
O(n) - we have to iterate through the array only once to put values into hashmap, and then we can fetch items in O(1) time.


SPACE COMPLEXITY:
O(n) - additional space is used a hashmap.


WHY BRUTE FORCE FAILS:
Brute force involves counting frequencies by checking through the entire array, which is inefficient for large arrays and time complexity would by O(n^2). This approach is optimal since we traverse the array only once and store all the counts for elements in a hashmap, so we reduce number of operations to be performed to be done in O(n) time.


WHAT I'D SAY IN AN INTERVIEW:
We have to return all the elements and their counts for a given array.
We use a hashmap to store all the unique elements in the array as keys and their counts as values, and returning the hashmap containing all key-value pairs.
Time complexity is O(n) since we only iterate through the array once. Space complexity is O(n) since additional space is used for a hashmap.
"""

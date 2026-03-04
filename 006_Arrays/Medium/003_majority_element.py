"""
INTUITION:
Given an array of length n, find the majority element of the array, majority element appears more than n/2 times in the array.


APPROACH:
This can be solved using Moore's Voting Algorithm. It says that one element will effectively cancel the occurrence of another element. if majority element exists, it cannot be fully cancelled.
1. Initialise:
    - element = nums[0]
    - count = 0
2. Loop from i=0 to n-1.
3. For each iteration,
    1. Update element if count == 0
    2. Check if current element is equal to element or not:
        - If true, increment count by 1.
        - If false, decrement count by 1.


EDGE CASES:
None
"""

# CODE SOLUTION:
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = nums[0]
        count = 0
        n = len(nums)

        for i in range(0, n):
            if count == 0:
                element = nums[i]

            if nums[i] == element:
                count += 1
            else:
                count -= 1

        return element


nums = [3, 2, 3]
print(Solution().majorityElement(nums))

"""
TIME COMPLEXITY:
O(n) - we find the majority element in a single array pass.


SPACE COMPLEXITY:
O(1) - no additional space was used or data structures were used.


WHY BRUTE FORCE FAILS:
Brute force involves checking the frequency for each element in the array, which can take O(n^2) time.
Better approach would be to iterate through the array once and store the frequencies in a hashmap. Then iterate through the hashmap and return the element with the highest frequency. This takes O(n) time and O(n) space.
Moore's voting algorithm is optimal approach since we find the majority element is a single array pass, taking O(n) time and O(1) space.


WHAT I'D SAY IN AN INTERVIEW:
For a given array, we have to find the element that appears more than n/2 times in the array.
We can find using Moore's voting algorithm. The occurrence of a number will cancel another number's occurrence too. So the number which survives the cancellation process is the majority element.
Time complexity is O(n) since we find the majority element in a single array pass. Space complexity is O(1) since no additional data structures were used.
"""

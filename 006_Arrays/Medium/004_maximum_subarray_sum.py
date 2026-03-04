"""
INTUITION:
For a given array, we have to find the maximum sum from all possible subarrays.


APPROACH:
This can be solved using Kadane's Algorithm. This algorithm checks for sums for each element as iterating the array. We compare sum and store the maximum sum. When this sum goes below zero, we reset to 0 as negative sum wont help identify maximum sum.
1. Initialise:
    - max_sum = -math.inf
    - current_sum = 0
2. Iterate from 0 to len(nums).
3. For each iteration:
    1. Add nums[i] to sum.
    2. Compare sum to max_sum and keep maximum.
    3. Check if current_sum < 0. If true, reset sum to 0.


EDGE CASES:
None
"""

# CODE SOLUTION:
import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -math.inf
        current_sum = 0

        for i in range(0, len(nums)):
            current_sum += nums[i]
            max_sum = max(max_sum, current_sum)

            if current_sum < 0:
                current_sum = 0

        return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(nums))


"""
TIME COMPLEXITY:
O(n) - we calculate the max subarray sum in a single pass of the array.


SPACE COMPLEXITY:
O(1) - no additional space is used.


WHY BRUTE FORCE FAILS:
Brute force involves finding all subarrays and then calculating their sum to compare for maximum sum, which takes O(n^2) time. Kadane's algorithm is optimal since we can find the maximum subarray sum is O(n) time by a single array pass.


WHAT I'D SAY IN AN INTERVIEW:
We have to find maximum subarray sum for a given array.
This problem can be solved optimally using Kadane's algorithm. We add current element to sum and check if sum > max_sum and update max_sum accordingly. If at any step sum < 0, we reset sum to 0 as a negative value wont help in finding the maximum sum.
Time complexity is O(n) as we find the max subarray sum in a single array pass, and space complexity is O(1) as no additional data structures were used.
"""

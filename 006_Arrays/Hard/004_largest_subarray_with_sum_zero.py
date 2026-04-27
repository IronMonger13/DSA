"""
INTUITION:
Given an array nums of length n, we have to find the length of the maximum subarray with sum 0.
We are also given the constraints that len(nums) > 0, and it can have both positive and negative integers.
This can be done using the prefix sum method.
If sum of a subarray is x, and another subarray within that subarray sums to x, that means the remaining portion must be 0.We calculate the length of that subarray and compare it with max length
Calculate prefix sum for each element and store it in a map with its index. If at any time prefix sum = 0, our new max length will be current index + 1.
Else check if prefix sum is in map is equal to a prefix sum in map, if it is, that means current index - index at that prefix sum is equal to 0, so get the length as current index - prefix sum's index store in map, and compare it to max length to get the maximum length.
If the prefix sum is not in map, add it to the map with its index


APPROACH:
1. Initialise-
    1. empty map (prefix_map = {})
    2. current_len = 0
    3. max_len = 0
    4. prefix_sum = 0
2. Loop from i = 0 to n (excluded).
3. Calculate prefix_sum as prefix_sum + nums[i]
4. Check if prefix sum is 0, if it is, update max_len as i + 1.
5. Else check if prefix sum exists in prefix_map. If it does, that means the remaining subarray is 0, so get current_len as i - prefix_map[prefix_sum], and compare it to max_len to keep the max length.
6. Else it means prefix sum is not in the map, so add it to the map storing it with its index.
7. Return max_len.


EDGE CASES:
None due to constraints, general solution handles everything.
"""

# CODE SOLUTION:
from typing import List


class Solution:
    def largest_subarray_with_sum_zero(self, nums: List[int]) -> List[List[int]]:
        prefix_map = {}
        current_len = 0
        max_len = 0
        prefix_sum = 0

        n = len(nums)

        for i in range(0, n):
            prefix_sum += nums[i]
            if prefix_sum == 0:
                max_len = i + 1
            else:
                if prefix_sum in prefix_map:
                    current_len = i - prefix_map[prefix_sum]
                    max_len = max(current_len, max_len)
                else:
                    prefix_map[prefix_sum] = i

        return max_len


nums = [9, -3, 3, -1, 6, -5]
print(Solution().largest_subarray_with_sum_zero(nums))


"""
TIME COMPLEXITY:
O(n) - we get the max length with a single array iteration


SPACE COMPLEXITY:
O(m) - additional space is used for a map, where m is the number of unique prefix sums.


WHY BRUTE FORCE FAILS:
Brute force includes checking each subarray sum, which takes O(n^2) time.
This approach is optimal since it takes O(n) time to find the length of max subarray and takes O(m) space for a map to store unique prefix sums.


WHAT I'D SAY IN AN INTERVIEW:
We are given an array nums of length n, and we have to find the max length of subarray with sum 0.
We solve this using the prefix sum method where check if prefix sum exists in the map or not, if it does, that means the remaining subarray is zero, and we find its length and compare with the max length. If the prefix sum does not exist in the map, then we add it to the map with its index.
Time complexity is O(n) since we find the max length in a single array pass, and space complexity is O(m) since additional space is used for map to store prefix sum with its index, where m is the number of unique prefix sums.
"""

"""
INTUITION:
Given a sorted array nums and a target element, we have to find the number of occurrences of target in nums.
We are given the constraints-
1. 0 <= nums.length <= 10^5
2. -10^9 <= nums[i] <= 10^9
3. nums is a non-decreasing array.
4. -10^9 <= target <= 10^9
This can be done using lower and upper bound concept of binary search.
We first find the lower bound of the target element, then we find the upper bound of the target element.
Then we check to ensure that the target element does exist in nums.
If they do, we return upper bound index - lower bound index, if they dont, we return 0.


APPROACH:
1. Calculate lower bound index (smallest index where element >= target).
2. Calculate upper bound index (smallest index where element > target).
3. Check if lower bound index does lie within the nums length, and lower bound element is equal to target-
    1. If false, return 0
    2. If true, return upper bound index - lower bound index.


EDGE CASES:
None due to constraints.
"""

# CODE SOLUTION:
from typing import List


class Solution:
    def lower_bound(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        lb = len(nums)

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb

    def upper_bound(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        ub = len(nums)

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub

    def count(self, nums: List[int], target: int) -> List[int]:
        lb = self.lower_bound(nums, target)
        ub = self.upper_bound(nums, target)

        if (lb == len(nums)) or (nums[lb] != target):
            return 0
        return ub - lb


nums = [2, 2, 3, 3, 3, 3, 4]
target = 3
print(Solution().count(nums, target))


"""
TIME COMPLEXITY:
O(log n) - finding lower bound takes up O(log n) time, and finding upper bound takes up another O(log n) time, which totals to 2 * O(log n), which can be simplified to O(log n).


SPACE COMPLEXITY:
O(1) - no additional space or data structures were used.


WHY BRUTE FORCE FAILS:
Brute force includes linearly traversing through the array to find the count of occurrences of the target element, which takes O(n) time, and does not use the property of the array being sorted.
This approach is optimal since we find the first and last occurrence of the target element in O(log n) time.


WHAT I'D SAY IN AN INTERVIEW:
We are given a sorted array nums and a target element, and we have to find the count of occurrences of the target.
This can be done by first finding the lower bound index of the target in nums, and then finding the upper bound index of target in nums. Lower bound is the smallest index where nums[index] >= target, and upper bound is the smallest index where nums[index] > target. Once we have the lower and upper bound index, we can check that the lower bound index is not equal to the hypothetical index, or lower bound element does equal to the target. If both are true, we return upper bound index - lower bound index, else we return 0.
Time complexity is O(log n) and space complexity is O(1).
"""

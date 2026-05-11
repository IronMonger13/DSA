"""
INTUITION:
Given a sorted array nums and a target, find the upper bound. Upper bound is the smallest index where nums[upper bound] > target.
This can be found using binary search. We eliminate the search space where elements are greater than target.


APPROACH:
1. Initialize -
    1. ans = len(nums)
    2. low = 0
    3. high = len(nums) - 1
2. Loop while low <= high.
3. Calculate mid as (low + high) // 2
4. If nums[mid] > target, that means mid might be a possible answer, so update ans to mid, and search in the left search space by updating high as mid - 1
5. Else update low as mid + 1, as that means mid element is lower than target, so all elements on the left must also be lower than target.
6. Return ans.


EDGE CASES:
None due to constraints.
"""

# CODE SOLUTION:
from typing import List


class Solution:
    def ub(self, nums: List[int], target: int) -> int:
        ans = len(nums)
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


nums = [1, 2, 2, 3]
target = 2
print(Solution().ub(nums, target))

"""
TIME COMPLEXITY:
O(log n) - we keep dividing the search space to find upper bound.


SPACE COMPLEXITY:
O(1) - no additional data structures are used.


WHY BRUTE FORCE FAILS:
Brute force includes performing linear search to find the upper bound, which takes O(n) time as it does not utilize the property of the array being sorted.
This approach is optimal since we keep dividing the search space to find upper bound, which takes O(log n) time.


WHAT I'D SAY IN AN INTERVIEW:
We are given a sorted array nums and a target. We need to find the upper bound. Upper bound is the smallest index where nums[upper bound] > target.
This can be solved using binary search algorithm. We divide the search space into two halves, and check mid value. If nums[mid] > target, we update our ans as mid and then look on the left side for a possible smaller index that satisfies the conditions. Else we look on the right side. We keep looping till low crosses high.
Time complexity is O(log n) and space complexity is O(1).
"""

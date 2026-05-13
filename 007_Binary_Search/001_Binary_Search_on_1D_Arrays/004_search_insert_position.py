"""
INTUITION:
Given a sorted array nums with all unique elements and a target, find the index at which target is present or should be placed such that the array remains sorted.
We are given the following constraints-
1. 1 <= nums.length <= 10^4
2. -10^4 <= nums[i] <= 10^4
3. nums contains distinct values sorted in ascending order.
4. -10^4 <= target <= 10^4
This problem can be solved by using binary search. We eliminate the search space where elements are lower than the target.


APPROACH:
1. Initialize
    1. low = 0
    2. high = len(nums) - 1
    3. ans = last index + 1 as default index
2. Loop while low <= high.
3. Calculate mid as (low + high) // 2.
4. If nums[mid] >= target, that means mid might be a possible ans, so we update ans as mid and eliminate the entire search space from mid to high as all elements in the search space would be greater than the target. Update high as mid - 1.
5. Else update low as mid + 1, as that would mean all elements are lower than the target, so ans would lie somewhere in the other search space.
6. Return ans.


EDGE CASES:
None due to constraints.
"""

# CODE SOLUTION:
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        ans = len(nums)

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans


nums = [1, 3, 5, 6]
target = 5
print(Solution().searchInsert(nums, target))


"""
TIME COMPLEXITY:
O(log n) - we keep eliminating half of the search space at each iteration.


SPACE COMPLEXITY:
O(1) - no additional data structures are used.


WHY BRUTE FORCE FAILS:
Brute force involves performing a linear search to find the index. It does not use the property of the array being sorted. Hence time complexity is O(n).
This approach is optimal since we keep dividing the search space in half at each iteration till we find the index. This takes only O(log n) time.


WHAT I'D SAY IN AN INTERVIEW:
We are given a sorted array nums with all unique elements and a target, and we have to find the index at which we can place the target such that the array is still sorted.
We use binary search for this problem. We divide the search space into two halves and check mid value. If nums[mid] >= target, that means the current index is a possible answer and we eliminate the search space from mid to high as all elements in the search space would be greater than target. Else we eliminate the search space from low to mid since all elements in that search space are smaller than the target.
Time complexity is O(log n) since we keep dividing the search space, and space complexity is O(1) since no additional data structures are used.
"""

"""
INTUITION:
Given a sorted array nums and a target x, we have to find:
1. Floor of x - the largest element smaller than or equal to x.
2. Ceil of x - the smallest element greater than or equal to x.
Since the array is sorted, we can use binary search to eliminate half of the search space at every step.
The ceil is essentially the lower bound of x.
The floor is the last element smaller than or equal to x.


APPROACH:
1. Create two binary search functions:
    - floor_value()
    - ceil_value()
2. For floor:
    - Initialize ans = -1
    - If nums[mid] <= x:
        mid can be a possible floor.
        Store nums[mid] in ans and search on the right side for a larger valid value.
    - Else search on the left side.
3. For ceil:
    - Initialize ans = -1
    - If nums[mid] >= x:
        mid can be a possible ceil.
        Store nums[mid] in ans and search on the left side for a smaller valid value.
    - Else search on the right side.
4. Return both floor and ceil.


EDGE CASES:
1. If no floor exists, return -1.
    Example: x smaller than every element.

2. If no ceil exists, return -1.
    Example: x greater than every element.
"""

# CODE SOLUTION:
from typing import List


class Solution:
    def floor_value(self, nums: List[int], x: int) -> int:
        low = 0
        high = len(nums) - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] <= x:
                ans = nums[mid]
                low = mid + 1
            else:
                high = mid - 1

        return ans

    def ceil_value(self, nums: List[int], x: int) -> int:
        low = 0
        high = len(nums) - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= x:
                ans = nums[mid]
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def getFloorAndCeil(self, nums: List[int], x: int):
        floor_ans = self.floor_value(nums, x)
        ceil_ans = self.ceil_value(nums, x)

        return [floor_ans, ceil_ans]


nums = [3, 4, 4, 7, 8, 10]
x = 5

print(Solution().getFloorAndCeil(nums, x))


"""
TIME COMPLEXITY:
O(log n) - binary search is used twice, once for floor and once for ceil.
So total time complexity is O(log n + log n), which simplifies to O(log n).


SPACE COMPLEXITY:
O(1) - no additional data structures are used.


WHY BRUTE FORCE FAILS:
Brute force involves traversing the entire array and checking every element to find the floor and ceil values.
This takes O(n) time.
Binary search is optimal because the array is already sorted, allowing us to eliminate half of the search space at every step and reduce the time complexity to O(log n).


WHAT I'D SAY IN AN INTERVIEW:
We are given a sorted array and a target x, and we need to find:
1. The floor → largest element less than or equal to x.
2. The ceil → smallest element greater than or equal to x.
Since the array is sorted, we can solve both using binary search.
For floor, whenever nums[mid] <= x, mid becomes a possible answer and we search on the right side for a larger valid value.
For ceil, whenever nums[mid] >= x, mid becomes a possible answer and we search on the left side for a smaller valid value.
Time complexity is O(log n) and space complexity is O(1).
"""

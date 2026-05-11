"""
INTUITION:
We are given a sorted array nums and a target element to be found. We have to return the index of the target element. If not present, we return -1.
We are given the constraints -
1. 1 <= nums.length <= 10^4
2. -10^4 < nums[i], target < 10^4
This can be done using binary search. It works on sorted data structures. We keep dividing the array till we find the element.
We initialize low and high and find the mid element and compare it to target, if mid element == target, we return the index, else we check if target is smaller than mid element. If true, our search space updates to low to mid - 1, else it updates to mid + 1 to high. We keep repeating this till low <= high.
If low crosses high, that means target element is not present and we return -1.


APPROACH:
1. Define a new function called bs for recursive calls.
2. Define base case - if low > high, return -1.
3. Calculate mid as (low + high) // 2.
4. Check if nums[mid] == target, if it is, return mid.
5. Else if nums[mid] > target, recursively call bs with search space from low to mid - 1.
6. Else recursively call bs with search space from mid + 1 to high.


EDGE CASES:
None due to constraints.
"""

# CODE SOLUTION:
from typing import List


class Solution:
    def bs(self, nums, low, high, target):
        if low > high:
            return -1

        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.bs(nums, low, mid - 1, target)
        else:
            return self.bs(nums, mid + 1, high, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.bs(nums, 0, len(nums) - 1, target)


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(Solution().search(nums, target))


"""
TIME COMPLEXITY:
O(log2n) - we keep dividing the search space into half each time, hence we take up only log2n time to find the element if present.


SPACE COMPLEXITY:
O(log n) - extra space is required for recursive call stack. Iterative approach for the same takes up O(1) time.


WHY BRUTE FORCE FAILS:
Brute force involves checking each element of the array from start to end, which takes up O(n) time.
This approach is optimal since we take up only O(log2n) time to find the element's index.


WHAT I'D SAY IN AN INTERVIEW:
We are given a sorted array and a target and we have to find the index of target in the array nums. If target is not present, we return -1.
We use binary search to solve this problem. We keep on dividing the search space into two parts and eliminate one half if the element is not present in it, by comparing mid element to target.
This takes up O(log2n) time to find the element if present. Iterative approach takes up O(1) space and recursive approach takes up O(log n) space since additional space is required for recursive stack.
"""

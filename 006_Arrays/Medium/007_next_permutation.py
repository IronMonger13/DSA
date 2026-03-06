"""
INTUITION:
For a given array nums, we have to find the lexicographically next permutation of the given array. This means if we have to check what will the next "dictionary" combination from the elements of the array that can be formed.
We are also told:
1. 1 <= nums.length <= 100
2. 0 <= nums[i] <= 100


APPROACH:
The goal is to find the next lexicographically greater permutation of the array.
1. Find the breakpoint (first decreasing element from the right):
    - Traverse the array from right to left and find the first index `ind` such that nums[ind] < nums[ind + 1].
    - This point is called the breakpoint because everything to the right of it is already in decreasing order.
    - If no such index exists (ind == -1), the array is the largest possible permutation. In that case, reverse the entire array to get the smallest permutation.
2. Find the element just larger than nums[ind]. Traverse from the end of the array and find the first element greater than nums[ind]. Swap that element with nums[ind].
3. Reverse the suffix. After the swap, the elements to the right of `ind` are still in decreasing order. Reverse the subarray from ind + 1 to the end to transform it into the smallest possible order.
This ensures the resulting array is the next lexicographically greater permutation.


EDGE CASES:
None
"""

# CODE SOLUTION:
from typing import List


class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        return nums

    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        ind = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break

        if ind == -1:
            nums = Solution().reverse(nums, 0, n - 1)
            return

        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break

        nums = Solution().reverse(nums, ind + 1, n - 1)

        return nums


nums = [1, 2, 3]
print(Solution().nextPermutation(nums))


"""
TIME COMPLEXITY:
O(n) - All of the operations are being performed in linear time. O(n) time is taken to find the breakpoint, another O(n) to find the element next largest to nums[ind], and another O(n/2) to reverse the array. So final time complexity is O(n + n + n/2), which simplifies to O(n).


SPACE COMPLEXITY:
O(1) -  since next permutation is found in place.

WHY BRUTE FORCE FAILS:
Brute force would generate all permutations of the array, sort them, and then locate the current permutation to find the next one. Generating permutations alone takes O(n!) time, making the approach extremely inefficient.
This approach is optimal since we iterate the array thrice in the worst case to find the next permutation, which takes O(n) time.


WHAT I'D SAY IN AN INTERVIEW:
We are asked to find the next lexicographical permutation of the given array.
The key observation is that permutations increase from right to left. So we first scan the array from the right to find the first position where nums[i] < nums[i+1]. This position is called the breakpoint. If no breakpoint exists, the array is already the largest permutation, so the next permutation will simply be the smallest one, which we get
by reversing the array.
If a breakpoint exists, we then look for the smallest element greater than nums[i] on the right side and swap them.
Finally, the suffix to the right of the breakpoint is reversed because it was originally in decreasing order, and reversing it gives the smallest possible arrangement.
This produces the next lexicographically greater permutation.
Time complexity is O(n) since we scan the array a constant number of times, and space complexity is O(1) because the permutation is modified in place.
"""

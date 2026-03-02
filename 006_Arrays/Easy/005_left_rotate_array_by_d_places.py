"""
INTUITION:
Given an array nums of length n and an integer k, right rotate nums by k places.


APPROACH:
This can be done in 3 simple steps of reversing arrays.
1. First ensure that k lies within the range of array's length as k=k%n.
2. Now first reverse the subarray for last k elements from index n-k to n-1.
3. Then reverse the subarray from index 0 to n-k-1, meaning till last element before kth index from end.
4. Now reverse the whole array.


EDGE CASES:
None
"""


# CODE SOLUTION:
class Solution:
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(nums, k: int):
        n = len(nums)
        k %= n

        Solution.reverse(nums, n - k, n - 1)
        Solution.reverse(nums, 0, n - k - 1)
        Solution.reverse(nums, 0, n - 1)

        return nums


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(Solution.rotate(nums, k))


"""
TIME COMPLEXITY:
O(n) - we only traverse through the entire array three times, which is O(k + (n-k) + n), which is O(2n), which can be simplified to O(n)


SPACE COMPLEXITY:
O(1) - array is rotated in place, no additional data structures used.


WHY BRUTE FORCE FAILS:
Brute force is inefficient since we rotate the array one element at ta time, and each rotation takes O(n) time. So to rotate array k times is O(n^2) time and O(n) space. This approach is optimal since we only reverse the array three times to rotate it k times, which takes O(n) time and O(1) space.


WHAT I'D SAY IN AN INTERVIEW:
We have to right rotate the given array k times.
This can be easily done by first reversing the array from n-k to n-1 index, and then from 0 to last index just before kth index, and then reversing the whole array again from 0 to last index. This gives us the array right rotated k times.
Time taken is O(n) since we only have to iterate through the array to perform the operations, and space is O(1) since no additional data structures were used, and rotation happened in place.
"""

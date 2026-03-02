"""
INTUITION:
For a given array nums, move all the zeroes to the end, preserving the order of the non-zero elements.


APPROACH:
1. Iterate through the array to find the occurrence of the first 0 in the array. If none found, return the array as it is.
2. Store the index of the first 0.
3. Initialise a non_zero variable and set it to first zero index found + 1.
4. Loop from first zero index element till the end of array.
5. Increment non_zero variable to find the first non zero element.
6. When found, swap non zero and zero elements in the array and increment both variables by 1.


EDGE CASES:
None
"""


# CODE SOLUTION:
class Solution:
    def moveZeroes(nums):
        n = len(nums)

        zero = -1
        for i in range(0, n):
            if nums[i] == 0:
                zero = i
                break

        if zero == -1:
            return

        non_zero = zero + 1
        while non_zero < n:
            if nums[non_zero] == 0:
                non_zero += 1
            else:
                nums[non_zero], nums[zero] = nums[zero], nums[non_zero]
                non_zero += 1
                zero += 1

        return nums


nums = [0, 1, 0, 3, 12]
print(Solution.moveZeroes(nums))


"""
TIME COMPLEXITY:
O(n) - we only iterate through the array once to find the first zero, which takes O(n) time, and then iterate through the array to swap zero and non-zero elements, which takes O(n) time. So total time taken is O(n + n), which is simplified to O(n).


SPACE COMPLEXITY:
O(1) - no additional space is used.


WHY BRUTE FORCE FAILS:
Brute force involves storing the non zero elements temporarily in another array, which takes O(n) space. This approach is optimal since we take the same amount of time to solve this (O(n)), we do it in place, meaning we dont take additional space.


WHAT I'D SAY IN AN INTERVIEW:
We have to move all the non-zero elements of the given array to the beginning and zeroes to the end, preserving the original order of the non-zero elements.
We iterate through the array to find the first zero of the array, if not found, that means we can return the array unchanged. If found, we store the index and start iterating from the next index. If a non-zero element is found, we swap it with the element stored in the zero variable index and increment both zero and non-zero variables by 1 to carry on with next iterations. If non zero isnt found, we simply increment non-zero index by 1 to check the next element of the array.
Time complexity is O(n) since we only iterate through the array and swap, both of which takes O(n) each. Space complexity is O(1) since no additional space is used.
"""

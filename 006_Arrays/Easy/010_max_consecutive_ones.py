"""
INTUITION:
For a given array of binary numbers, find length of max consecutive ones.


APPROACH:
1. Set a variable max_ones to 0 to keep track of max 1s length.
2. Set another variable count to 0 to keep track of current 1s lengths.
3. Iterate through the array.
4. For each iteration, if element = 1, increment count by 1 and find max of count and max_ones.
5. If for any iteration element = 0, set count to 0.


EDGE CASES:
None
"""


# CODE SOLUTION:
class Solution:
    def findMaxConsecutiveOnes(nums) -> int:
        max_ones = 0
        count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_ones = max(count, max_ones)
            else:
                count = 0

        return max_ones


nums = [1, 0, 1, 1, 0, 1]
print(Solution.findMaxConsecutiveOnes(nums))


"""
TIME COMPLEXITY:
O(n) - we only iterate through the array once to keep track of counts of consecutive ones.


SPACE COMPLEXITY:
O(1) - no additional space is used.


WHY BRUTE FORCE FAILS:
Brute force involves comparing all subarrays with all elements one to find the length of the subarray has that has highest number of ones, which can take O(n^2) time. This approach is optimal since we can find length of max consecutive ones in a single array pass, which takes O(n) time.


WHAT I'D SAY IN AN INTERVIEW:
We have to find the maximum number of consecutive ones in an array containing only binary numbers.
We have to iterate through the array and for each consecutive one, increment count by 1 and update the max ones variable to check for maximum count. If we encounter a zero in the array, we reset count back to 0.
Time complexity is O(n) since we find the length of max consecutive ones in a single array pass. Space complexity is O(1) since no additional data structures were used.
"""

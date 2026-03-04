"""
INTUITION:
Given an array containing only three elements, 0, 1 and 2, we have to sort the array.


APPROACH:
This can be solved using Dutch National Flag algorithm. Imagine an array divided into 4 segments using variables called low, mid and high. All elements in the array between 0 and low-1 are 0s, all elements between low and mid-1 are 1s, and all elements between high+1 to n-1 are 2s. The elements between mid and high are unsorted, which is what our actual array will be.
1. Initialise:
    - mid = 0
    - low = 0
    - high = n-1
2. Loop while mid <= high.
3. For one iteration, only one case can happen:
    - arr[mid] == 0
    - arr[mid] == 1
    - arr[mid] == 2
4. If:
    - arr[mid] == 0, swap arr[mid] and arr[low], and move both low and mid one place forward, as low's last element would now be the swapped 0.
    - arr[mid] == 1, just move mid one place forward as it is in the correct place.
    - arr[mid] == 2, swap arr[mid] and arr[high], and move high one place backwards, as high's first element would now be the swapped 2.


EDGE CASES:
None
"""

# CODE SOLUTION:
from typing import List


class Solution:
    def sortColors(self, nums: List[int]):
        n = len(nums)

        mid = 0
        low = 0
        high = n - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        return nums


nums = [2, 0, 2, 1, 1, 0]
print(Solution().sortColors(nums))


"""
TIME COMPLEXITY:
O(n) - we sort the array in a single pass.


SPACE COMPLEXITY:
O(1) - no additional space is used, or O(n) if we count the size of array we return, however it is not used in the algorithm hence, O(1).


WHY BRUTE FORCE FAILS:
Brute force involves sorting the whole array using a sorting algorithm. The most optimal sorting algorithms are merge sort and quick sort, which take O(n log n) time O(log n) space and O(n log n) time O(1) space respectively.
Better approach would be keep a track of count of 0s, 1s and 2s in three different variables, and then put the count of 0s and 1s and 2s in order, which will take O(2n) time total.
Dutch National Flag Algorithm is optimal since we iterate through the array only once and get the array sorted, which takes O(n) time and O(1) space, and does so in a single array pass.


WHAT I'D SAY IN AN INTERVIEW:
We are given an array consisting of 3 elements - 0,1 and 2, and we have to sort the array in ascending order.
This can be done using the Dutch National Flag Algorithm- where we assume our array to be a subarray of a large sorted array with only one unsorted subarray. Then we assign low, mid and high pointers and swap values and/or move pointers till mid pointer crosses high, and when it does, our array will be sorted.
Time complexity is O(n) since we sort the array in a single pass. Space complexity is O(1) since no additional space is used, or O(n) if we count the size of the array which we return.
"""

"""
INTUITION:
Given a sorted array of length n, we have to remove the duplicates in place, and keep all the unique elements in the array. The remaining non-unique elements can be replaced with anything, just the first unique elements matter.


APPROACH:
This can be solved using two pointer approach.
1. Set a pointer i at 0th index.
2. Iterate from j = 1 till j < n.
3. For each iteration, check if nums[i] != nums[j]. If they are not equal, set nums[i+1] = nums[j], and increment i by 1.


EDGE CASES:
n = 1 - return 1
"""


# CODE SOLUTION:
class Solution:
    def removeDuplicates(nums) -> int:
        n = len(nums)

        if n == 0 or n == 1:
            return n

        i = 0

        for j in range(1, n):
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1

        return i + 1


nums = [1, 2, 2]
print(Solution.removeDuplicates(nums))


"""
TIME COMPLEXITY:
O(n) - we modify the array using two pointers in a single iteration.


SPACE COMPLEXITY:
O(1) - no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force involves storing the elements of the array in set, in which insertion takes n time, and takes n space. It is used to keep track of all the unique elements. This approach is optimal since we modify the array in a single pass using two pointers, which takes O(n) time and O(1) space. 


WHAT I'D SAY IN AN INTERVIEW:
For a given sorted array in non-descending order, we have to find out the unique elements in the array, and the first k elements of the array should be the unique elements, where k is the number of unique elements.
We can set a pointer at index 0 (i). Then iterate j from 1 till the end of array and check if arr[i] is not equal to arr[j], then set arr[i+1] to arr[j], and move i to the next index. After the iterations are complete, i+1 is the final number of unique elements.
Time complexity is O(n) since all operations are performed in a single pass of the array. Space complexity is O(1) since the array was modified in place and no additional data structures were used.
"""

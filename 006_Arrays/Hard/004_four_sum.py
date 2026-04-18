"""
INTUITION:
Given an array nums of length n, we have to find four elements whose sum is equal to a given target.
We have the following constraints-
1. 1 <= nums.length <= 200
2. -10^9 <= nums[i] <= 10^9
3. -10^9 <= target <= 10^9
This is similar to three sum, which uses the principle of using two pointers as used in two sum.
First we lock in two pointers, first at index 0 and second at index 1. Then we move third and fourth pointers to find the sum that is equal to target. We also sort the array in the beginning to avoid duplication. If at any iteration our sum is greater than target, that means we need to lower the sum, so we decrease fourth by 1. If sum is lesser than target, that means we need to increase the sum, hence we increase third by 1. We repeat this till third and fourth cross. When the first iteration is over, we move on to the next unique value for second, and repeat the same process. When all iterations for the second pointer are done as well, that is when we move our first pointer to the next unique value, and rinse and repeat. If at any point of time, sum is equal to target, we push the quadruplet into ans list and keep decreasing fourth and increasing third till they are at a new unique value or they cross each other.


APPROACH:
1. Sort nums.
2. Initialise an empty list (ans).
3. Lock in the first pointer to the first element of the array and loop from 0 to n-3(not included). Check if first > 0 and nums[first - 1] == nums[first]. If true, continue, as it means we are picking up duplicate values when moving forward with the iteration. If false, we can move forward.
4. Lock in the second pointer at first + 1 position and loop from first + 1 to n-2)not included). Check if second > first + 1 and nums[second - 1] == nums[second]. If true, continue, as it means we are picking up duplicate values when moving forward with the iteration. If false, we can move forward.
5. Set third to second + 1 and fourth to n - 1.
6. Loop till third crosses fourth.
7. Calculate four_sum as nums[first] + nums[second] + nums[third] + nums[fourth].
8. If four_sum > target, fourth--.
9. If four_sum < target, third++.
10. If four_sum == target, push the quadruplets to ans and increase third and decrease fourth till both of them are at a new value or they cross each other.


EDGE CASES:
None due to constraints and all cases are handled by general solution.
"""

# CODE SOLUTION:
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for first in range(0, n - 3):
            if first > 0 and nums[first - 1] == nums[first]:
                continue
            for second in range(first + 1, n - 2):
                if second > first + 1 and nums[second - 1] == nums[second]:
                    continue
                third = second + 1
                fourth = n - 1
                while third < fourth:
                    four_sum = nums[first] + nums[second] + nums[third] + nums[fourth]
                    if four_sum > target:
                        fourth -= 1
                    elif four_sum < target:
                        third += 1
                    else:
                        ans.append(
                            [
                                nums[first],
                                nums[second],
                                nums[third],
                                nums[fourth],
                            ]
                        )
                        third += 1
                        fourth -= 1
                        while third < fourth and nums[third - 1] == nums[third]:
                            third += 1
                        while third < fourth and nums[fourth] == nums[fourth + 1]:
                            fourth -= 1
        return ans


nums = [1, 0, -1, 0, -2, 2]
target = 0
print(Solution().fourSum(nums, target))


"""
TIME COMPLEXITY:
O(n^3) - we need to iterate through three nested loops to control the positions of the four pointers, which takes O(n^3). We also sort the array in the beginning, which takes O(n log n) time. So total time complexity is O(n log n + n^3), which is simplified to O(n^3).


SPACE COMPLEXITY:
O(1) - auxiliary space since no additional data structures were used for finding out the quadruplets.
O(m) - output space since we used a list to return quadruplets, where each element of the list is another list of 4 elements, and m is the number of quadruplets. So total output space is O(m * 4), which is O(m).


WHY BRUTE FORCE FAILS:
Brute force includes picking up each element and finding quadruplets, which takes O(n^4) time and since we dont need duplicate quadruplets, a set is used before returning the list, so space complexity becomes O(m + m).
Better approach would be to store the elements between the second last and last pointer in a hashset, which takes O(n^3) time and O(n + m) space for hashset's elements and the resultant list.
This approach is optimal since it finds the quadruplets in O(n^3) time and uses only O(m) space to return the resultant list, where m is the number of unique quadruplets.


WHAT I'D SAY IN AN INTERVIEW:
We are given an array and we need to return a list of all unique quadruplets who sum to the given target.
This can be solved in a similar way to three sum problem, which uses two pointers that keep moving as to get the desired sum, and first pointer is locked in place until inner iteration is complete. Similarly, we lock first and second pointers in place, and keep moving third and fourth pointers to get the desired sum till they cross each other. When this happens, we move second pointer to the next unique value, and repeat the same process. Once all iterations for the second pointer are complete, we move the first pointer, which is being controlled by the outermost loop, and repeat the same things. If at any point sum>target, we reduce fourth pointer by 1, and if sum is lesser than target, we increase third pointer by 1. If sum == target, we append the quadruplet to the resultant list and then we keep on increasing third and decreasing fourth till they are both having new unique values or till they cross each other.
Time complexity is O(n^3) since we need to run three loops to control the four pointers, and space complexity is O(1) auxiliary space since no additional space is used for finding quadruplets, and O(m) for output space where m is the number of unique quadruplets.
"""

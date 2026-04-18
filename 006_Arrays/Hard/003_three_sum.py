"""
INTUITION:
Given an array nums of length n, we have to find out three elements whose sum is 0 and indexi != indexj != indexk.
We are given the constraints -
1. 3 <= nums.length <= 3000
2. -10^5 <= nums[i] <= 10^5
This can be done sorting the array and then fixing first pointer and using two pointers to find the sum 0, similar to how we approach two sum. Once second and third pointers cross, we move to the next iteration for first pointer where the element is not the same as the previous one and repeat second and third pointer approach again. We repeat this till all iterations for the first pointer are complete.


APPROACH:
1. Sort the given array to avoid duplication of triplets.
2. Initialise a new list to store triplets (ans).
3. Loop using start pointer from 0 to n-2 (not included).
4. Increment start if its greater than 0 and nums[start - 1] == nums[start] to avoid picking up duplicate values for the first pointer.
5. If above condition is false, it means that start now is on a different element, so set mid as start + 1, and end to n - 1.
6. While mid < end, calculate three_sum as nums[start] + nums[mid] + nums[end]
7. If three_sum == 0, append them into ans, and mid++ and end--. Then to ensure we dont pick up duplicate values, pick up the next different num for both mid and end.
8. If three_sum < 0, means we have to increase the sum, so we increment mid by 1.
9. If three_sum > 0, means we have to decrease the sum, so we decrement end by 1.


EDGE CASES:
None due to constraints and everything is handled by the general solution.
"""


# CODE SOLUTION:
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for start in range(0, n - 2):
            if start > 0 and nums[start - 1] == nums[start]:
                continue
            else:
                mid = start + 1
                end = n - 1
                while mid < end:
                    three_sum = nums[start] + nums[mid] + nums[end]
                    if three_sum == 0:
                        ans.append([nums[start], nums[mid], nums[end]])
                        mid += 1
                        end -= 1
                        while mid < end and nums[mid - 1] == nums[mid]:
                            mid += 1
                        while mid < end and nums[end] == nums[end + 1]:
                            end -= 1
                    elif three_sum > 0:
                        end -= 1
                    else:
                        mid += 1
        return ans


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))


"""
TIME COMPLEXITY:
O(n^2) - we need O(n log n) time to sort the array, and then O(n^2) time to find all the triplets, which takes O(n log n) + O(n^2) time, which simplifies to O(n^2) time.


SPACE COMPLEXITY:
O(m) - we need to store the triplets in a list, where each element is of length 3 and m is the number of unique triplets found. So total space used is 3*O(m), which simplifies to O(m).


WHY BRUTE FORCE FAILS:
Brute force includes checking valid triplets for each element, which takes O(n^3) time.
Better approach would be to use a hashmap to store all the triplets in sorted order in a set data structure, which takes O(n^2) time and O(m) space for set and O(m) for the list to be returned, where m is the number of unique triplets.
Current solution is the optimal approach since it takes O(n^2) time to find all the triplets and doesnt use teh additional space used by the set data structure, so final space taken is only to return the list, which is O(m), where m is the number of unique triplets.


WHAT I'D SAY IN AN INTERVIEW:
We are given an array nums of length n and we have to find all the triplets in such a way their sum = 0 and index of first element != index of second element != index of third element.
Core idea is to sort nums first as to avoid picking up duplicate elements later and fix one pointer and use the two sum approach to find the sum where if sum of three elements is zero then we push those triplets into the list to be returned, and increase second pointer and decrease third pointer by 1, and keep changing these values till we get a distinct value than previous or till they cross each other. If however sum is greater than 0, we have to decrease the sum so we decrease third pointer by 1, but if sum is less than zero, that means we have to increase the sum so we increase second pointer by 1. Once done with this inner iteration, we increase the position of first pointer till we get a different value than the previous one.
Time complexity is O(n^2), and space complexity is O(m), where m is the number of unique triplets.
"""

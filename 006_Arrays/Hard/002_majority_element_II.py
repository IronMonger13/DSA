"""
INTUITION:
Given an array nums of length n, we have to find out the elements that appear more than n/3 times in the array.
We are also given these constraints -
1. 1 <= nums.length <= 5 * 104
2. -10^9 <= nums[i] <= 10^9
At max, we can only have 2 elements as answer from the entire array.
We can have two elements initialise with their counts equal to 0, and any element that is not either of those 2 cancels out their count, and if any element is equal to either of those elements, we increase the count of that element by 1.
Perform a manual check to ensure count of those elements is greater than n/3.
Sort those elements and return them in a list.


APPROACH:
1. Initialise -
    1. element1 = 0
    2. element2 = 0
    3. count1 = 0
    4. count2 = 0
2. Loop inside nums to iterate through elements (num)
3. If count1 == 0 and num != element2 then set element1 to num and increase count by 1
4. If count2 == 0 and num != element1 then set element2 to num and increase count by 1
5. If we encounter a num that is either element1 or element2, we increase the respective element's count by 1
6. If no above condition is satisfied, that means current num cancels the count of both of these elements, hence count1-- and count2--.
7. After iteration is complete, initialise an empty list (and) and set count1 and count2 to 0 for manual checking of the elements to ensure they appear more than n/3 times.
8. Loop inside nums to iterate through the elements (num) and if count1 > n/3, append element1 to ans, and if count2 > n/3, append element2 to ans.
9. Sort ans and return it.


EDGE CASES:
1. n = 0 - empty list is returned
2. n = 1 - return nums[0]
"""

# CODE SOLUTION:
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [nums[0]]

        element1 = float("-inf")
        element2 = float("-inf")
        count1 = 0
        count2 = 0

        for num in nums:
            if count1 == 0 and num != element2:
                element1 = num
                count1 += 1
            elif count2 == 0 and num != element1:
                element2 = num
                count2 += 1
            elif num == element1:
                count1 += 1
            elif num == element2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = 0
        count2 = 0

        for num in nums:
            if num == element1:
                count1 += 1
            elif num == element2:
                count2 += 1

        min_required = n // 3
        ans = []
        if count1 > min_required:
            ans.append(element1)
        if count2 > min_required:
            ans.append(element2)

        if len(ans) == 2 and ans[0] > ans[1]:
            ans[0], ans[1] = ans[1], ans[0]

        return ans


nums = [3, 2, 3]
print(Solution().majorityElement(nums))


"""
TIME COMPLEXITY:
O(n) - we are finding the majority elements that appear more than n/3 times in a single iteration (O(n)) and checking the count of candidate elements by iterating through the array again, which takes another O(n) time. So total time is O(n) + O(n), which simplifies to O(n).


SPACE COMPLEXITY:
O(1) -  since no additional data structures were used, other than a list whose maximum size can not be greater than 2 elements.


WHY BRUTE FORCE FAILS:
Brute force includes picking up each element and checking its count in the entire array, which takes O(n^2) time.
Better approach would be to use a hashmap to store the counts of each unique element, which would take O(n) time and O(n) space.
Current solution is the optimal approach since we iterate through the array once to find the candidate elements, and once to verify the candidate element's occurrence in the array is greater than n/3, which takes another O(n). So total time taken is O(n) and space complexity is O(1).


WHAT I'D SAY IN AN INTERVIEW:
We are given an array nums of length n and we have to find out the elements that appear greater than n/3 times.
At max we can have only 2 elements. Lets take n=8 for example. 8//3 = 2, so we need to find elements that appear at least 3 times. 3+3=6, so if two elements appear three times, that means the third element will appear 2 times. So for any length of nums, we can have at max 2 elements. We start by initializing element1 and element2 to -inf and their counts (count1 and count2) to 0. If count1 equals 0 and current num != element2, we set element1 to current num. Similarly, if count2 == 0 and current num != element1, we set element2 to current num. Then we check if current num is equal to element1 or element2, if it is, we increase the respective count by 1. If not, we decrease both counts by1 as it means the current num cancels the count of both the elements. Then we perform a manual check to ensure that the candidate elements do appear more than n/3 times. If they do, we append them into an empty list and sort the list and return the list.
Time complexity is O(n) since we find candidate elements in a single iteration and then validate their counts through another iteration. Space complexity is O(1) since no additional data structures are used other than a list whose size can be at maximum 2.
"""

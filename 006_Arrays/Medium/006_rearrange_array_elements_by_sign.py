"""
INTUITION:
We are given an array nums with equal number of positive and negative numbers, we have to arrange elements such that array's first element is positive, second element is negative, and so on. We also have to preserve the order of positive and negative numbers. We are also told:
1. Array should start with positive element.
2. 2 <= nums.length <= 2 * 10^5
3. nums.length is even
4. 1 <= |nums[i]| <= 105
5. nums consists of equal number of positive and negative integers.


APPROACH:
This can be solved using two pointer approach. All the positive elements are even indexed and all the negative elements are odd indexed. We iterate and check if element is greater than 0 or lesser than 0, and accordingly place them in the new result array and increment pos or neg index by 2.
1. Initialise:
    - pos_index = 0
    - neg_index = 1 (this helps us preserve pos and neg indexing)
    - res array = [0] * len(nums)
2. For each num in nums, check if num is greater than 0 or not:
    - If true, insert num at pos_index in res and increment pos_index by 2.
    - If false, insert num at neg_index in res and increment neg_index by 2.



EDGE CASES:
None
"""

# CODE SOLUTION:
from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos_index = 0
        neg_index = 1
        res = [0] * n

        for num in nums:
            if num > 0:
                res[pos_index] = num
                pos_index += 2
            else:
                res[neg_index] = num
                neg_index += 2

        return res


nums = [3, 1, -2, -5, 2, -4]
print(Solution().rearrangeArray(nums))


"""
TIME COMPLEXITY:
O(n) - we build the res array in a single array pass.


SPACE COMPLEXITY:
O(n) - additional n space is used to return the answer.


WHY BRUTE FORCE FAILS:
Brute force involves storing all the positive elements in a single array and negative elements in another array, and combining them to form the correct array. This takes O(2n) time and O(n) space. Time complexity is simplified to O(n).
This approach is slightly better as we use same time and same space (O(n)), but we form the res array in a single array pass, as compared to brute force, where we passed the array twice.


WHAT I'D SAY IN AN INTERVIEW:
We are given an array with equal number of positives and negatives. We have to rearrange the array in such a way that positive and negatives sit right next to each other in the array, starting with positive elements, and keeping the order of positive and negatives preserved. 
We can simply create a res array with length equal to nums, and start with all values 0 in the array. We set pos_index to 0 and neg_index to 1 to keep the format of alternate positives and negatives, and start iterating through nums. We check for all num in nums, if num > 0, we insert it into res array at pos_index and increment pos_index by 2. Similarly we check and perform operations for when num < 0.
Time complexity is O(n) since we form the res array in a single array pass. Space complexity is O(n) as additional n space is used to return the res array.
"""

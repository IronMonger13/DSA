"""
INTUITION:
We are given an array nums of length n, with one element being repeated and one element is missing iin the interval [1, n].
We can do this by solving two equations as
1. eq1 = sum of elements in nums - sum of elements from 1 to n
2. eq2 = sum of square of elements in nums - sum of square of elements from 1 to n
So we get repeating - missing = eq1 and repeating^2 - missing^2 = eq2
When we open eq2, we get (repeating - missing)(repeating + missing) = eq2. We already have eq1 = repeating - missing, so we can derive eq2 as eq2/eq1.
Now we have repeating + missing and repeating - missing as eq2 and eq1 respectively.
We can use find repeating as (eq1 + eq2) / 2, and from the remaining equation, we can find missing.


APPROACH:
1. Initialise -
    1. s = 0
    2. s2 = 0
    3. missing = 0
    4. repeating = 0
2. Calculate sum in s and squared sum in s2 by iterating through nums
3. Calculate sum of numbers from 1 to n as n(n+1)/2
4. Calculate sum of square of numbers from 1 to n as n(n+1)(2n+1)/6
5. Define eq1 as s - sn
6. Define eq2 as (s2 - s2n)/ eq1
7. Find repeating as (eq1 + eq2)/2
8. Find missing as eq2 - repeating
9. Return [missing, repeating]



EDGE CASES:
None due to constraints
"""

# CODE SOLUTION:
from typing import List


class Solution:
    def missing_and_repeating(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = 0
        s2 = 0
        missing, repeating = 0, 0

        for num in nums:
            s += num
            s2 += num * num
        sn = (n * (n + 1)) // 2
        s2n = (n * (n + 1) * ((2 * n) + 1)) // 6

        eq1 = s - sn
        eq2 = (s2 - s2n) // eq1
        repeating = (eq1 + eq2) // 2
        missing = eq2 - repeating

        return [missing, repeating]


nums = [3, 5, 4, 1, 1]
print(Solution().missing_and_repeating(nums))


"""
TIME COMPLEXITY:
O(n) - we find missing and repeating in a single array pass.


SPACE COMPLEXITY:
O(1) - no additional space or data structures were used, other than a list of size 2 for returning missing and repeating elements.


WHY BRUTE FORCE FAILS:
Brute force includes checking each number from 1 to n in nums, which can take O(n^2) since each number would take an entire array pass.
Better approach would be to use hashmap to store the frequencies of the numbers in nums. Element with frequency 2 would be repeating digit, and element in interval [1, n] which doesnt exist in the hashmap will be the missing number. This approach taken O(n) time and O(n) space.
This approach is optimal since we use math equations to get missing and repeating numbers, which takes O(n) time for a single array pass, and O(1) space.


WHAT I'D SAY IN AN INTERVIEW:
We are given an array nums in the interval [1, n] and we have to find out the missing number and repeating number in nums.
We can find sum of all elements in nums and subtract it from sum of all elements from 1 to n for our first equation. Then we can find sum of square of all elements in nums, and sum of square of all elements from 1 to n. This will be our second equation. We can use these two equations to solve and find missing and repeating elements.
Time complexity is O(n) since we find missing and repeating in a single array pass. Space complexity is O(1) since no additional space or data structures are used.
"""

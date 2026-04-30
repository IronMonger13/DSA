"""
INTUITION:
We are given two sorted arrays nums1 and nums2, and we need to merge nums2 into nums1 in-place.
nums1 has enough extra space at the end to hold all elements of nums2.
Since both arrays are already sorted, the key idea is to avoid extra sorting and instead place elements in their correct position directly.
The largest elements will always be at the end. So instead of merging from the front (which would overwrite values), we merge from the back.


APPROACH:
1. Initialise three pointers:
    - i = m - 1 → last valid element in nums1
    - j = n - 1 → last element in nums2
    - k = m + n - 1 → last position in nums1
2. While both i >= 0 and j >= 0:
    - Compare nums1[i] and nums2[j]
    - Place the larger element at nums1[k]
    - Move the corresponding pointer (i or j) and decrement k
3. If any elements remain in nums2 (j >= 0):
    - Copy them into nums1

4. Return nums1


EDGE CASES:
Handled implicitly by the logic:
- If nums1 has no valid elements (m = 0), nums2 is directly copied
- If nums2 is empty (n = 0), nums1 remains unchanged
"""

# CODE SOLUTION:
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(Solution().merge(nums1, m, nums2, n))

"""
TIME COMPLEXITY:
O(m + n) - each element from both arrays is processed exactly once.


SPACE COMPLEXITY:
O(1) - merging is done in-place without using extra space.


WHY BRUTE FORCE FAILS:
Brute force involves copying all elements into a new array and then sorting, which takes O((m + n) log(m + n)) time and O(m + n) space.
This is inefficient compared to the optimal in-place merge which avoids sorting and runs in linear time.


WHAT I'D SAY IN AN INTERVIEW:
1. The problem asks us to merge two sorted arrays into nums1 in-place.

2. Since both arrays are sorted, I use a two-pointer approach from the end to avoid overwriting values. I compare the largest elements from both arrays and place the larger one at the end of nums1.

3. Time complexity is O(m + n) since we traverse both arrays once, and space complexity is O(1) as the merge is done in-place.
"""

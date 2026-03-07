"""
INTUITION:
FInd the longest consecutive sequence of elements that exists in an unsorted array.
We are also told:
1. 0 <= nums.length <= 10^5
2. -10^9 <= nums[i] <= 10^9


APPROACH:
1. Initialise:
    - an empty set data structures
    - max_count = 0
2. Iterate through the array and store all elements in the set.
3. Iterate through the set and check if current_element - 1 exists in the set or not.
    - If it does, that means current element is not the first element of a sequence.
    - If it doesnt, that means current element is the first element of a sequence. Count till the num+1 exists in the set. Track the max length of the sequence.


EDGE CASES:
None
"""

# CODE SOLUTION:
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set()
        max_count = 0

        for num in nums:
            st.add(num)

        for num in st:
            if num - 1 not in st:
                count = 1
                next_num = num
                while next_num + 1 in st:
                    count += 1
                    next_num += 1
                max_count = max(max_count, count)

        return max_count


nums = [100, 4, 200, 1, 3, 2]
print(Solution().longestConsecutive(nums))

"""
TIME COMPLEXITY:
O(n) - we iterate through the array once to store all elements in set, and once per element in the set to get length of longest subsequence. Lookup in a set is O(1), so total time taken is O(n + n + 1), which is O(n). 


SPACE COMPLEXITY:
O(n) - additional space is used for set data structure, which can have len(nums) elements in the worst case.


WHY BRUTE FORCE FAILS:
Brute force includes keep checking the next element for each element to check for the longest consecutive sequence, which takes O(n^2) time and O(1) space.
Better approach would be sorting the array and then checking for each distinct sequence, which would take O(n log n) time and O(1) space.
Optimal approach would be using set to store the elements and performing lookups from the start of a sequence to find the longest consecutive sequence, which takes O(n) time and O(n) space.


WHAT I'D SAY IN AN INTERVIEW:
We have to find longest consecutive sequence that exists in the given array.
Idea is to store the elements in a set, look in set if the current element is the beginning of a sequence or not. If it is, keep looking for next number till we dont find the next number, and keep tracking count while doing this. Finally compare count and max_count to store the maximum value and return it.
Time complexity is O(n) as we iterate through the array to store elements and then iterate through the set to check for each element. Space complexity is O(n) since we used additional n space for set data structure.
"""

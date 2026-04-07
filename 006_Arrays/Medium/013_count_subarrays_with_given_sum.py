"""
INTUITION:
We need to count how many subarrays have sum equal to k. We use prefix sum: at any index i, we keep track of the total sum from index 0 to i. If at index i, current sum = S, and we have seen a previous prefix sum = S - k, then the subarray between those two indices has sum = k.
So the problem reduces to: “How many times have we seen (current_sum - k) before?”
We store prefix sums and their frequencies using a hashmap.


APPROACH:
1. Initialize a hashmap (prefix_map) to store frequency of prefix sums.
2. Set prefix_map[0] = 1 (to handle subarrays starting from index 0).
3. Initialize:
    - current_sum = 0
    - count = 0
4. Traverse the array:
    - Add current element to current_sum.
    - Check if (current_sum - k) exists in hashmap:
        - If yes, add its frequency to count.
    - Update hashmap: increment frequency of current_sum.
5. Return count.


EDGE CASES:
- Subarray starts from index 0 → handled by prefix_map[0] = 1
- Negative numbers → sliding window fails, prefix sum works
- All elements = 0 and k = 0 → multiple overlapping subarrays
"""

# CODE SOLUTION:
from collections import defaultdict


class Solution:
    def subarraySum(self, nums, k):
        prefix_map = defaultdict(int)
        prefix_map[0] = 1

        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num

            if (current_sum - k) in prefix_map:
                count += prefix_map[current_sum - k]

            prefix_map[current_sum] += 1

        return count


nums = [1, 1, 1]
k = 2
print(Solution().subarraySum(nums, k))


"""
TIME COMPLEXITY:
O(n) - we traverse the array once, and each hashmap operation is O(1) on average.


SPACE COMPLEXITY:
O(n) - in worst case, all prefix sums are unique and stored in hashmap.


WHY BRUTE FORCE FAILS:
Brute force checks all subarrays using two loops, which is O(n^2).
Prefix sum reduces this to O(n) by avoiding recomputation.


WHAT I'D SAY IN AN INTERVIEW:
The problem asks to count number of subarrays whose sum equals k.
I use prefix sum + hashmap to track how many times (current_sum - k) has appeared before.
Time complexity is O(n) and space complexity is O(n).
"""

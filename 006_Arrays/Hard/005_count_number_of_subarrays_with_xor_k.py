"""
INTUITION:
We are given an array and a value k, and we need to count how many subarrays have XOR equal to k.

Key observation:
If prefix_xor at index i is X, and there exists a previous prefix_xor = Y such that:
X ^ Y = k
Then the subarray between those indices has XOR = k.

Rewriting:
Y = X ^ k

So the problem reduces to:
For each prefix_xor, check how many times (prefix_xor ^ k) has appeared before.


APPROACH:
1. Initialize:
    - prefix_map = hashmap to store frequency of prefix_xor values
    - prefix_map[0] = 1 (to handle subarrays starting from index 0)
    - prefix_xor = 0
    - count = 0

2. Traverse the array:
    - Update prefix_xor using XOR with current element
    - Compute required_xor = prefix_xor ^ k
    - If required_xor exists in prefix_map:
        → add its frequency to count
    - Store/update prefix_xor in prefix_map

3. Return count


EDGE CASES:
- Subarray starting from index 0 → handled by prefix_map[0] = 1
- All elements are 0 and k = 0 → multiple valid overlapping subarrays
- Negative numbers → XOR logic still works (unlike sliding window)
"""

# CODE SOLUTION:
from typing import List
from collections import defaultdict


class Solution:
    def count_subarray_with_xor_k(self, nums: List[int], k: int) -> int:
        prefix_map = defaultdict(int)
        prefix_map[0] = 1
        prefix_xor = 0
        n = len(nums)
        count = 0

        for i in range(0, n):
            prefix_xor ^= nums[i]
            count += prefix_map[prefix_xor ^ k]
            prefix_map[prefix_xor] += 1

        return count


nums = [4, 2, 2, 6, 4]
k = 6
print(Solution().count_subarray_with_xor_k(nums, k))

"""
TIME COMPLEXITY:
O(n) - we traverse the array once, and each hashmap operation (lookup and insert) takes O(1) on average.


SPACE COMPLEXITY:
O(n) - in the worst case, all prefix_xor values are unique and stored in the hashmap.


WHY BRUTE FORCE FAILS:
Brute force involves checking all possible subarrays and calculating XOR for each, which takes O(n^2) time.

Even with prefix XOR optimization, generating all subarrays still leads to O(n^2).
Using hashing reduces this to O(n) by avoiding recomputation and leveraging previously seen prefix XOR values.


WHAT I'D SAY IN AN INTERVIEW:
1. The problem asks to count the number of subarrays whose XOR equals k.

2. I use prefix XOR and a hashmap. 
    If prefix_xor at index i is X, I check how many times (X ^ k) has occurred before.
    That tells me how many subarrays ending at i have XOR = k.

3. Time complexity is O(n) due to single pass and constant-time hashmap operations.
    Space complexity is O(n) for storing prefix XOR frequencies.
"""

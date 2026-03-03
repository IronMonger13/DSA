"""
INTUITION:
For a given array, find length of the largest subarray whose sum is equal to k.


APPROACH:
This can be solved using prefix sum and hashmap.
1. Initialise:
    - empty hashmap
    - sum = 0
    - max_len = 0
2. Loop from i = 0 to len(arr).
3. Add ith element to sum to get the prefix sum.
4. Check if sum is equal to k, if true, max_len will be i+1.
5. If false, check if prefix sum already exists in the hashmap as sum-k. If it exists, length of th subarray would be i - the index stored for prefix sum - k, and compare this with max_len to keep max value.
6. If false, store the prefix sum in hashmap, but only if it doesnt already exist in the map. This will ensure we always take the earliest occurrence of prefix sum to get max length.

EDGE CASES:
len(arr) = 0 - return 0, meaning no subarray will have sum k
"""


# CODE SOLUTION:
def longest_subarray(arr, k):
    n = len(arr)

    if n == 0:
        return 0

    prefix_map = {}
    sum = 0
    max_len = 0

    for i in range(0, n):
        sum += arr[i]

        if sum == k:
            max_len = i + 1

        if sum - k in prefix_map:
            max_len = max(max_len, i - prefix_map[sum - k])

        if sum not in prefix_map:
            prefix_map[sum] = i

    return max_len


arr = [6, -2, 2, -8, 1, 7, 4, -10]
k = 0
print(longest_subarray(arr, k))


"""
TIME COMPLEXITY:
O(n) - we only iterate through the array once to calculate the prefix sum and other operations.


SPACE COMPLEXITY:
O(n) - additional space is needed for a hashmap, where worst case is we store all the prefix sums (no duplicate sums), which will take at max n spaces in the hashmap.


WHY BRUTE FORCE FAILS:
Brute force is inefficient as it involves finding all the subarrays and calculating their sum and then comparing the lengths of these subarrays to return the max length, which takes up O(n^2) time.
Prefix sum and hashing approach is optimal here since we iterate the array only once to find the prefix sum and store it in the hashmap, which takes more space as compared to brute force approach (O(n) and O(1) respectively), but it takes significantly lower time of only O(n) (linear time as compares to n^2).
Hashing and prefix sum is optimal for because the array has negative numbers. If we had only positives, the optimal approach would be using two pointers sliding window approach as it takes O(n) time and O(1) space, but it fails when negative numbers are present in the array.


WHAT I'D SAY IN AN INTERVIEW:
We are given an array with both positive and negative numbers and k, we have to find the length of the largest subarray whose sum is equal to k.
We simply calculate the prefix sum of all elements. If we find sum == k when calculating sum, we update max_len to index+1. If not, we check if prefix sum - k exists in hashmap, if it does, that means the subarray indexed from i - index of prefix sum - k to i is the length of the subarray, which we can compare to max_len to find the maximum length. If the prefix sum doesnt already exist in the array, we insert in the hashmap.
Time complexity is O(n) since we need to iterate through the array once to calculate the prefix sum. Space complexity is O(n) since additional space is used for storing prefix sums in the hashmap.
"""

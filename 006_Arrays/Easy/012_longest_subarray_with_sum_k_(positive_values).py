"""
INTUITION:
For a given array, we have to return the length of the longest subarray whose sum is k.


APPROACH:
This problem can be solved using the sliding window (two pointers) technique.
Note: This works only when all array elements are non-negative.

1. Initialize:
    left = 0
    sum = arr[0]
    max_len = 0

2. Maintain a window [left … right] such that at every step:
    sum = sum of elements inside this window.

3. The invariant is:
    Always ensure sum <= k.
    If sum becomes greater than k, the window is invalid and must be repaired.

4. Iterate right from 0 to n-1:
    - While sum > k:
        Subtract arr[left] from sum
        Move left forward
        (Shrink aggressively until the window becomes valid again.)
    - If sum == k:
        Update max_len with (right - left + 1)
    - Add arr[right] to sum (expand the window).

5. Continue expanding right to explore larger windows.

The key idea:
Shrinking is corrective (to restore sum <= k).
Expanding is exploratory (to find longer valid subarrays).


EDGE CASES:
len(arr) = 0 - return 0, meaning subarray doesnt exist.
"""


# CODE SOLUTION:
def longest_subarray(arr, k):
    n = len(arr)

    if n == 0:
        return 0

    left = 0
    right = 0
    sum = arr[0]
    max_len = 0

    while right < n:
        while left <= right and sum > k:
            sum -= arr[left]
            left += 1

        if sum == k:
            max_len = max(max_len, right - left + 1)
        right += 1

        if right < n:
            sum += arr[right]

    return max_len


arr = [10, 5, 2, 7, 1, 9]
k = 15
print(longest_subarray(arr, k))


"""
TIME COMPLEXITY:
O(n) - each element is added and/or removed from the array at max once, so total iterations become O(<2n), which simplifies to O(n).


SPACE COMPLEXITY:
O(1) - no extra space is used.


WHY BRUTE FORCE FAILS:
Brute force involves finding all the subarrays and their sums, and then comparing their lengths where sum of a subarray is equal to k, which takes O(n^2) time.
Better approach would be to store the prefix sum in a hashmap, which would take O(n) time and O(n) space.
Two pointer approach is optimal in this case because all numbers are positive, and for such two pointer approach runs in O(n) time and O(1) space. If however we had negative numbers too, better approach of using hashmap would be optimal since two pointer doesnt work for negative numbers, as it works on the assumption that shrinking a window would decrease the sum and vice versa, but this might not happen with negative numbers, hence going against the hypothesis.


WHAT I'D SAY IN AN INTERVIEW:
For a given array and k, we have to find the length the of the largest subarray whose sum is equal to k. All digits of the given array are positive numbers.
Main idea is to use two pointers to keep a window to keep track of the sum of subarray, expanding when sum<k, shrinking when sum>k, and recording length when sum==k.
We start with first element as sum, and firstly check if our window is valid by ensuring sum <= k, if not we aggressively shrink the window as we know further expanding the window wont do any good. When sum<=k, we check for equality, if sum and k are equal, we record the length and update the max_len as max of previous max_len and current window size. Then we by default increment j as long as it in within bounds of array size to expand the window to explore further opportunities of subarrays whose sum == k and length might be greater.
Time complexity is O(n) since each element is added and/or removed from the array only once. Space complexity is O(1) since no additional space is used.
"""

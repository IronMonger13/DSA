"""
INTUITION:
For a given array and target, we have to find two indices whose sum in the array is equal to target.


APPROACH:
This can be solved using the idea that for index i, if target-nums[i] exists in hashmap, then i and target-nums[i] are the indices whose sum is equal to target. It basic mathematical property that if a + b = c, then a = c - b.
1. Initialise empty hashmap.
2. Iterate from i=0 to n-1.
3. Check if target-arr[i] exists in map.
    - If true, return i and target-arr[i] from the map as array
    - If false, add arr[i] to the map with its index i.


EDGE CASES:
None
"""


# CODE SOLUTION:
class Solution:
    def twoSum(nums, target: int):
        n = len(nums)
        mpp = {}

        for i in range(0, n):
            if target - nums[i] in mpp:
                return [i, mpp[target - nums[i]]]
            else:
                mpp[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9

print(Solution.twoSum(nums, target))


"""
TIME COMPLEXITY:
O(n) - we have to iterate only once through the entire array to check for each element if target-element exists in hashmap.


SPACE COMPLEXITY:
O(n) - additional space is used to store elements of nums with their index in hashmap.


WHY BRUTE FORCE FAILS:
Brute force involves checking each element with all other elements to find the indices whose sums are equal to target. This takes up O(n^2) time. Using hashmap is optimal since we can iterate through the array in O(n) time and store the elements in the hashmap and later check from hashmap if target-nums[i] exists in O(1) lookup time.


WHAT I'D SAY IN AN INTERVIEW:
For a given array nums and a target, we have to find the two indices whose elements, when summed are equal to target.
This can be solved using the basic mathematical property that if a + b = c, then a = c - b. If target-nums[i] exists in the hashmap, then index i and index of target-nums[i] are the required indices. When we start iterating through the array, we first check if target-nums[i] exists in the map or not. If it does, we return the indices are discussed above, if not, we store nums[i] with its index i in the hashmap.
Time complexity is O(n) since we only have to iterate through the array once to store the elements in the hashmap. Space complexity is O(n) since additional space is required to store elements in the hashmap.
"""

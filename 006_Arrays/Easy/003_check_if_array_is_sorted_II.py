"""
INTUITION:
For a given array of length n, determine if the array was originally in non-decreasing order (non-decreasing means ascending order but with duplicates allowed).


APPROACH:
This can be solved by the fact that if the array was originally sorted and then rotated, the array can have at max 1 drop (drop mean nums[i] > nums[i+1]).
1. Initialise a drop variable to 0 to keep track of number of drops happening when traversing though the array.
2. Run a loop from 0 to n-1.
3. If nums[i] > nums[(i+1)%n], increment drop by 1. The modulo n is to compare the last element to nums to the first one so to complete a full cycle of the array.
4. If at any point, we get drop > 1 , that means the array was not originally sorted.


EDGE CASES:
n = 1 - return true.
"""


# CODE SOLUTION:
class Solution:
    def check(nums) -> bool:
        n = len(nums)
        drop = 0

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                drop += 1

            if drop > 1:
                return False

        return True


nums = [2, 1, 3, 4]
print(Solution.check(nums))

"""
TIME COMPLEXITY:
O(n) - since all operations are performed in a single pass of the array.


SPACE COMPLEXITY:
O(1) - no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force is inefficient since it involves moving each element from the start to the end to simulate the array rotation and then checking if the array is sorted or not, which takes O(n^2) time. This approach is optimal since we have to iterate through the array only once, which takes only O(n) time.


WHAT I'D SAY IN AN INTERVIEW:
We have to determine that if the given array was originally sorted before being rotated k time, where k can be any whole number.
We can solve this by the fact that a sorted and rotated array can have at max 1 drop, and a drop means arr[i] > arr[i+1]. We compare each element to its next one in a single iteration of the array, and for last element, we compare it to the first element by wrapping it around with modulo n. We automatically return true when n = 1 as single element is always sorted.
Time complexity is O(n) since all operations are performed in a single of the array. Space complexity is O(1) since no additional data structures were used.
"""

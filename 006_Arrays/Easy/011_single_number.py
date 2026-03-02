"""
INTUITION:
For a given array, find the number that appears only once while all other numbers appear twice.


APPROACH:
This can be solved using XOR operator. XOR between two numbers is 0 (a^a=0) and XOR between 0 and any number is the number (0^a=a).
1. Iterate through the array and store XOR of all numbers in a variable.
2. Return the variable, as it is the only remaining single element.


EDGE CASES:
None
"""


# CODE SOLUTION:
class Solution:
    def singleNumber(nums) -> int:
        xor = 0

        for num in nums:
            xor ^= num

        return xor


nums = [4, 1, 2, 1, 2]
print(Solution.singleNumber(nums))


"""
TIME COMPLEXITY:
O(n) - we only have to iterate once through the array to find xor of all numbers.


SPACE COMPLEXITY:
O(1) - no additional space is used.


WHY BRUTE FORCE FAILS:
Brute force involves checking for each element whether its copy exists in the array or not, which takes O(n^2) time as for each element, we have to iterate n times, and there are n elements.
Better approach would be to use a hashmap, which involves iterating through the array and storing all the elements and their frequencies in a hashmap, which takes O(n) space and O(n) time.
This approach is optimal since we use the XOR operation to find the only single element in the array, which takes O(n) time and O(1) extra space.


WHAT I'D SAY IN AN INTERVIEW:
We are given an array in which every number is present two times, except for one number. We have to find the single number in the array.
Core idea behind the solution is to use XOR operator, as a^a is 0 and 0^a is a. Using these properties, we can cancel out all the double elements and will be left with only the single element after iterating through the entire array.
Time complexity is O(n) since we only iterate through the array once. Space complexity is O(1) since no additional data structures or extra space was used.
"""

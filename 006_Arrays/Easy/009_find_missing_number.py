"""
INTUITION:
For a given array of size n - 1, one number is missing between 1 and n (inclusive). Find that missing number.


APPROACH:
1. Use mathematical formula of sum of first n natural numbers to find total of first n numbers as n(n+1)/2.
2. Iterate through the array to find the sum of all elements.
3. Return the difference.


EDGE CASES:
None due to constraints
"""


# CODE SOLUTION:
class Solution:
    def missingNum(arr):
        n = len(arr)

        total_sum = ((n + 1) * (n + 2)) // 2

        arr_sum = 0
        for i in arr:
            arr_sum += i

        return total_sum - arr_sum


arr = [1, 2, 3, 5]
print(Solution.missingNum(arr))


"""
TIME COMPLEXITY:
O(n) - we iterate only once to find sum of all elements of the array.


SPACE COMPLEXITY:
O(1) - no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force involves looping from 1 to n, and checking which value for iteration does not exist in the array, which in worst case takes O(n^2) time. Using this approach is optimal since we can find the missing number in a single array iteration.


WHAT I'D SAY IN AN INTERVIEW:
We have to find the missing number in the array from 1 to n (n inclusive).
Main idea is to use the mathematical property of sum of first n natural numbers to find the sum, and subtracting the sum of all elements present in the array.
Time complexity is O(n) since we only iterate through the array once to find the sum of array elements. Space complexity is O(1) since no additional data structures were used.
"""

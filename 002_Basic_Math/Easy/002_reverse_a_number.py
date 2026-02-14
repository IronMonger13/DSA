"""
INTUITION:
We have to reverse the given number.


APPROACH:
Store the number in another variable to check for positive and negative later.
Initialise a variable where we will store the reversed number (rev).
Run a loop till number becomes 0.
Use % to get the last digit out of the number, add it to rev as rev * 10 + num % 10. This will give the last digit from num, and we can add it to rev to get its correct position.
Change num as num//10.
If original number was -ve, set reversed number as 0 - rev.


EDGE CASES:
n = 0 - 0
Reversed number is greater than or lesser 32-bit signed integer, return 0
"""


# CODE SOLUTION:
class Solution:
    def reverse(x: int) -> int:
        if x == 0:
            return 0

        num = abs(x)
        rev = 0

        while num != 0:
            rev = rev * 10 + (num % 10)
            num //= 10

        if x < 0:
            rev = 0 - rev

        if rev > pow(2, 31) - 1 or rev < pow(-2, 31):
            return 0

        return rev


print(Solution.reverse(123))


"""
TIME COMPLEXITY:
O(log n) since we iterate over the number of digits available in the number.


SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force is optimal since we iterate over the available number of digits, which takes only O(log n) time.


WHAT I'D SAY IN AN INTERVIEW:
We have to reverse the number given to us.
We use modulo operation to get the last digit of the number, and add it to 10 * rev, and change num by integer dividing it by 10. When num becomes zero, check if original number was -ve, if it is, subtract reversed number from 0, and check if it lies inside the 32 bit signed integer range, if not, then return 0. We already return 0 if x is 0.
Time complexity of O(log n) is optimal since we have to only iterate over the number of digits of the number given to us, and space complexity is O(1) since no additional data structures were used.
"""

"""
INTUITION:
Check if the given number is palindrome or not (palindrome means reads the same forwards and backwards).


APPROACH:
Store the given number in another variable (num).
Reverse the number by first creating a variable to store the reversed number (rev) and then running a loop while num is not equal to 0, and inside the loop, take modulo to extract the last digit of the number, multiply it by 10 and add it to rev, and integer divide num by 10 to remove the last digit.
After looping, check if original number and reversed number are same.


EDGE CASES:
x < 0 - return false
x >= 0 and x < 10 - return true
numbers ending in 0 - false
"""


# CODE SOLUTION:
class Solution:
    def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        if x >= 0 and x < 10:
            return True
        if x != 0 and x % 10 == 0:
            return False

        num = x
        rev = 0

        while num != 0:
            rev = rev * 10 + num % 10
            num //= 10

        return x == rev


print(Solution.isPalindrome(10))


"""
TIME COMPLEXITY:
O(log n) since we have to iterate only over the digits of the given number.


SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
The approach is optimal since we only iterate over the number for the number of digits it has.


WHAT I'D SAY IN AN INTERVIEW:
We have to check if the given number is palindrome or not. A palindrome is when it reads the same when read from forwards or backwards.
First reverse the number using modulo operation to extract the last digit, and adding it to 10 * rev. Once we are out of the loop, check if the reversed number is equal to the original number. We automatically return true if number is positive (including 0) and less than 10, and return false if number is -ve.
Time complexity is O(log n) which is optimal since we only have to iterate over the number of times as the number of digits in the given number. Space complexity is O(1) since no additional data structures were used.
"""

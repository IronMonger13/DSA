"""
INTUITION:
Check if string, after removing all non-alphanumeric characters, is palindrome or not, meaning reads same forwards and backwards.


APPROACH:
This problem can be solved using two pointer approach.
Initialize two pointers at 0th index and len(string)-1 called start and end respectively.
Loop while start < end
For each iteration:
1. Check if character at start and end are alphanumeric or not. If they are not, increment start and decrement end by 1 till they are.
2. Check if start and end characters in lowercase are equal. If they are not equal, return false, else increment start and decrement end by 1.


EDGE CASES:
len(string) = 1 - return true
"""

# CODE SOLUTION:
import re


class Solution:
    def isPalindrome(s: str) -> bool:
        if len(s) == 1:
            return True

        start = 0
        end = len(s) - 1

        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1

            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1

        return True


s = "A man, a plan, a canal: Panama"

print(Solution.isPalindrome(s))


"""
TIME COMPLEXITY:
O(n) since we have to perform only n number of operations.


SPACE COMPLEXITY:
O(1) - no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force is inefficient as we have to create a new string in reversed order to compare with the string, which adds another O(n) space. Two pointer is optimal since we skip this creation of another string to check for palindrome.


WHAT I'D SAY IN AN INTERVIEW:
We have to check if the string is a palindrome or not, meaning reads same forwards and backwards.
This can be solved optimally using two pointer approach.
First we initialise two pointers at the start and end of the string. We loop while start < end, and for every iteration, we first set the start and end pointers to the next alphanumeric position by incrementing start and decrementing end by 1 till they reach an alphanumeric character. Then we check if characters in lowercase at start and end are equal. If not, we return false meaning it is not a palindrome. If they are equal, we increment start and decrement end by 1 to prepare for the next iteration. When all iterations are complete, we return true, meaning the string is a palindrome. We return true if length of s is 1.
Time complexity is O(n) since we are performing n number of operations, and space complexity is O(1) since no additional data structures are used.
"""

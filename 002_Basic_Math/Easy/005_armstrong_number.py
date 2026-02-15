"""
INTUITION:
Check if a number is an armstrong number or not (armstrong number is when number equals sum of each digit, individually raised to the power of number of digits).


APPROACH:
1. Preserve the original number by storing it in num variable.
2. Count number of digits in num and store in variable called count.
3. Bring back the original value in num again from the preserved original number.
4. Initialise a new variable called armstrong to 0.
5. Loop till num reaches 0.
6. Inside each iteration, update the value of armstrong as armstrong + (last digit raised to power of count), and update num as num//10
7. After all iterations are done, return true if armstrong == original number, and false if not.


EDGE CASES:
n < 10 - return true
"""


# CODE SOLUTION:
class Solution:
    def isArmstrong(n):
        if n < 10:
            return True

        num = n
        count = 0

        while num != 0:
            count += 1
            num //= 10

        num = n
        armstrong = 0

        while num != 0:
            armstrong += pow(num % 10, count)
            num //= 10

        return n == armstrong


print(Solution.isArmstrong(370))

"""
TIME COMPLEXITY:
O(log n) since we have to perform operations only the number of times as number of digits in n.


SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
This approach is optimal as we have to perform operations only as number of times as the number of digits in n.


WHAT I'D SAY IN AN INTERVIEW:
We have to check if the given number is armstrong number or not. Armstrong number is when sum of each digit raised to the power of count of digits is equal to the given number.
First we get the count of the digits in the given number. Then we modulo operation to extract the last digits, raise it to the power of the number of digits, and add it to our armstrong number, which was initialized at 0 before looping, and then integer divide the number by 10 to get ready for the next iteration. Once num reaches 0, we check if armstrong number is equal to original given number, and return true if they are equal, else false. We return true automatically if number is less than 10 since any single digit number is already an armstrong number.
Time complexity of O(log n) is optimal since we only perform operations as the number of digits in the given number, and space complexity is O(1) since no additional data structures were used.
"""

"""
INTUITION:
Check if a number is prime or not, i.e. number is completely divisible only by 1 and itself.


APPROACH:
If a number is prime, that means its only divisors should be 1 and itself.
1. Initialise an empty array to store divisors.
2. Loop from 2 to sqrt(n)
3. For each loop iteration, check if n%i == 0. If it is, return false.


EDGE CASES:
n = 1 - false
n = 2 or 3 - return true
"""


# CODE SOLUTION:
def prime_number(n):
    if n == 1:
        return False
    if n < 4:
        return True

    for i in range(2, int(pow(n, 1 / 2)) + 1):
        if n % i == 0:
            return False

    return True


print(prime_number(9))

"""
TIME COMPLEXITY:
O(sqrt(n)) since we need to perform only sqrt(n) number of operations in worst case which takes sqrt(n) time.


SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force fails as we iterate from 1 to n to check for all divisors, which takes n number of operations. This approach is optimal since we perform sqrt(n) number of operations in worst case as any number than sqrt(n) would never divide n other than n itself.


WHAT I'D SAY IN AN INTERVIEW:
We have to check if a number is prime or not, meaning number is only divisible by 1 and the number itself.
We iterate from 2 till sqrt(n) and check if any number divides n. If it does, we return false as that would mean there is a third number that divides n other than n and 1 between 2 and sqrt(n). We also early return if n < 4 since 1 is not prime (false), 2 and 3 are prime numbers (true).
Time complexity is O(sqrt(n)) since we only perform sqrt(n) number of operations, which makes it optimal. Space complexity is O(1) since no additional data were used.
"""

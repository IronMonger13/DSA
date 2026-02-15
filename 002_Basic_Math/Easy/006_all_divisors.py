"""
INTUITION:
Print all divisors of n.


APPROACH:
1. Initialize 2 empty array to store divisors, first to store first half of the pair of divisors in ascending order, and second to store second pair of divisors in descending order.
2. Loop from 1 to sqrt(n).
3. If i fully divides n, push i to the array.
4. Check if n//i and i are distinct, if it is, push n//i in the array. This avoids pushing duplicate value in the array in case of a perfect square.
5. Concatenate both arrays, by appending the last indexed number in descending ordered array to 0th indexed number.


EDGE CASES:
n = 1 - return [1]
"""


# CODE SOLUTION:
def all_divisors(n):
    if n == 1:
        return [1]

    arr_asc = []
    arr_desc = []

    for i in range(1, int(pow(n, 1 / 2)) + 1):
        if n % i == 0:
            arr_asc.append(i)

            if n // i != i:
                arr_desc.append(n // i)

    for i in range(len(arr_desc) - 1, -1, -1):
        arr_asc.append(arr_desc[i])

    return arr_asc


print(all_divisors(36))

"""
TIME COMPLEXITY:
O(2 * sqrt(n)) since we only have to perform sqrt(n) number of operations and then sqrt(n) to concatenate both the arrays to get the array in sorted order, which simplifies to O(sqrt(n)).


SPACE COMPLEXITY:
O(2*sqrt(n)) since we have to store divisors, which simplifies to O(sqrt(n)).


WHY BRUTE FORCE FAILS:
Brute force fails because we iterate from 1 to n, in which takes O(n) number of operations to perform. This approach is optimal since we perform operation only sqrt(n) number of times, which takes O(sqrt(n)) time.


WHAT I'D SAY IN AN INTERVIEW:
We have to print all the numbers from 1 to n which fully divide n.
This can be done by the principle that if i divides n completely, n//i will also completely divide n.
We loop from 1 to sqrt(n) and for each value of i, we check if it fully divides it by n. If it does, we append i in the first array and check if n/i is equal to i. If it is not, we append n//i to the second array. Then append elements of the second array in reverse order into the first array to get our sorted array of all divisors. If n is 1, we simply return an array of only one element - [1].
Time complexity of O(sqrt(n)) is optimal since we only have to perform sqrt(n) number of operations to get all divisors, and space complexity is O(sqrt(n)) as we had to create new arrays to store the divisors.
"""

"""
INTUITION:
Reverse an array of length n, meaning the first element becomes last and last becomes first and so on.


APPROACH:
This can be done effectively using the two pointer approach.
Initialize 2 pointes, start and end at 0th index and n-1 index of the array respectively.
Loop while start < end.
For each iteration, swap value at start and end, increment start and decrement end by 1.


EDGE CASES:
n = 0 - nothing is printed.
n = 1 - return array as it is.
"""


# CODE SOLUTION:
def reverse_an_array(n, arr):
    if n == 0:
        return
    if n == 1:
        return arr

    start = 0
    end = n - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr


arr = [5, 4, 3, 2, 1]
n = len(arr)

print(reverse_an_array(n, arr))


"""
TIME COMPLEXITY:
O(n/2) which can be simplified to O(n). This is because we have to perform only n/2 number of operations to reverse the array.


SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
Brute force is inefficient as it involves iterating through the entire array from end to start and storing the numbers in a separate array, meaning it takes additional O(n) space. Two pointer approach is optimal since we reverse the array in place meaning no use of additional data structures, and we only have to perform n/2 number of operations.


WHAT I'D SAY IN AN INTERVIEW:
We have to reverse an array, meaning the first number becomes last and last becomes first and so on.
The optimal approach is to use two pointers.
We set two variables, one at the start of the array and one at the end of the array, and we only iterate when start < end. For each iteration, swap number at the start and end index, and increment start and decrement end by 1 for the next iteration. After the iterations are complete, we return the array, which is now reversed. We return nothing if n=0, meaning array is empty. We return the array as it is when n=1, meaning array has only 1 element.
Time complexity is O(n) which is optimal since we are only performing n/2 operations. Space complexity is O(1) since no additional data structures were used.
"""

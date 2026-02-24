"""
INTUITION:
Sort a given array in ascending order using selection sort.


APPROACH:
Principle - Select the minimum element from the array and swap it with the current iteration value in the array. When all iterations are complete, the array will be sorted.
Run an outer loop from i=0 to second last element of the array (len(arr)-2).
For each iteration, run an inner loop from i to the last element (len(arr)-1).
Find the smallest element in this range, and swap its position with value at index i.


EDGE CASES:
len(arr) = 0 - return the empty array
"""


# CODE SOLUTION:
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp

    return arr


arr = [4, 5, 6, 1, 2]
print(selection_sort(arr))


"""
TIME COMPLEXITY:
O(n^2) - we traverse through the entire array once for all elements except last, which takes O(n - 1) time. For each iteration, we compare all the following elements, which also takes O(n - k) time, where k is the number of elements that have already been checked. So total time taken is O((n-1) + (n-2) + ... + O(1)), which is equal to O(n(n-1)/2), which simplifies to O(n^2).


SPACE COMPLEXITY:
O(1) since no additional data structures were used.


WHY BRUTE FORCE FAILS:
Selection sort always performs n^2 comparisons regardless of input order, so it is inefficient compared to O(n log n) algorithms like merge sort or quicksort.


WHAT I'D SAY IN AN INTERVIEW:
We have to sort the given array in ascending order using selection sort.
We run an outer loop to iterate through the array, and an inner loop to find the smallest number. Once we get the smallest number, we swap the smallest number with the current value at the array in the outer loop. Once all the iterations are complete, we have an array sorted in ascending order. If length of given array is 0, we return an empty array meaning array is already empty.
Time complexity is O(n^2) since we traverse once through the entire array, and for each iteration, we traverse through the remaining array to find the smallest number, which takes O(n^2) time. Space complexity is O(1) since no additional data structures were used.
"""

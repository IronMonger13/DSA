"""
INTUITION:
Sort the given array using insertion sort.


APPROACH:
Principle - Keep swapping the element to the left until the element is in the correct position.
Run a outer loop from i=1 to len(arr).
Run an inner loop from j=i  while j>0 and arr[j]<arr[j-1].


EDGE CASES:
len(arr) = 0 - return empty array.
len(arr) = 1 - return the array containing the single element, which is already sorted.
"""


# CODE SOLUTION:
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

    return arr


arr = [7, 4, 1, 5, 3]
print(insertion_sort(arr))


"""
TIME COMPLEXITY:
O(n^2) - first swap will perform 1 swap, second operation will perform 2 swaps, and so on. So total swaps to be performed is 1+2+...+n. Thus time complexity becomes O(n(n-1)/2), which simplifies to O(n^2). Best case time complexity would be O(n), since we only traverse the array once and no swaps happen, meaning the array is already sorted.


SPACE COMPLEXITY:
O(1) - no additional data structures were used.


WHY BRUTE FORCE FAILS:
Any input for insertion sort, except an already sorted array, would take O(n^2) time, which is inefficient when compared to other sorting algorithms like merge sort, which sort the array in O(n log n) time.


WHAT I'D SAY IN AN INTERVIEW:
We have to sort the given array in ascending order using insertion sort.
We pick up each element through the outer loop, and place it into its correct position using the inner loop by swapping the element with its previous element if the element is smaller than the previous one or till the element reaches 0th index.
Time complexity is O(n^2) since we the number of swaps to be performed is the sum of n natural numbers, which is n(n-1)/2, which simplifies to O(n^2). Best case time complexity is O(n) since we only traverse the array once and no swaps happen, meaning the inner loop did not execute. This means array is already sorted. Space complexity is O(1) since no additional data structures were used and sorting happened in place.
"""

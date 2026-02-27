"""
INTUITION:
Sort a given array in ascending order using quick sort.


APPROACH:
Principle - divide the array and keep placing elements smaller and equal to the pivot element on left side and elements larger than the pivot element on right side.
Define a function that takes arr, high and low as parameters.
Place the pivot element in the right place by moving all elements smaller than the pivot on left side and all elements larger than the pivot element on the right side of the array:
1. Pick up the first element as pivot element.
2. Start a pointer (i) from low and a pointer (j) from high
3. Loop while i < j
4. Find the next element on right side of i index which is greater than the pivot element, and next element on left side of j index which is lesser than the pivot element.
5. If i is till smaller than j, swap arr[i] and arr[j].
6. Repeat this till i and j are equal or cross each other.
7. Once crossed, swap pivot element with the index where i and j intersected.
8. Store its position as partition index.
Recursively call the array from low to partition index - 1 to sort the left side of the array, and from partition index + 1 to high to sort right side of the array.
This will return the resulted array in sorted ascending order.


EDGE CASES:
len(arr) = 0 - return empty array (handled by general solution).
"""


# CODE SOLUTION:
def partition(arr, low, high):
    i = low
    j = high
    pivot = low

    while i < j:
        while i < high and arr[i] <= arr[pivot]:
            i += 1

        while j > low and arr[j] > arr[pivot]:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[pivot], arr[j] = arr[j], arr[pivot]

    return j


def qs(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)
        qs(arr, low, partition_index - 1)
        qs(arr, partition_index + 1, high)


def quick_sort(arr):
    low = 0
    high = len(arr) - 1

    qs(arr, low, high)
    return arr


arr = [4, 6, 2, 5, 7, 9, 1, 3]
print(quick_sort(arr))


"""
TIME COMPLEXITY:
O(n log n) - time taken for recursive calls is log n, and each recursive call performs n operations to place the element in the correct position in the array. So total time complexity is O(n log n).


SPACE COMPLEXITY:
O(log n) - additional log n stack space is used for recursive calls.


WHY BRUTE FORCE FAILS:
Brute force is inefficient since it involves comparing each element to all the other elements to place it in its correct position, which takes O(n^2) time. Even algorithm like merge sort is nt optimal since it takes O(n log n) time to sort the array, which is the same as time taken by Quicksort, merge sort does it in O(n) space since an additional space is used for a temp array. But quicksort takes only O(log n) stack space for recursive calls, making it optimal approach to sort an array.


WHAT I'D SAY IN AN INTERVIEW:
We have to sort the given array in ascending order using quick sort algorithm.
Quick sort relies on picking a pivot element, placing in its correct position by moving all the smaller elements on the left side and all the larger elements on the right side. Then recursively call the function for the array of smaller elements and array of larger elements. This will place all the elements at their correct positions, giving an array sorted in ascending order.
Time taken to sort the array is O(n log n) since there are log n recursive calls, and each recursive call takes n operations to place the element in the correct position. Space complexity is O(log n) since even though the array is sorted in place, additional stack space of log n is required for the recursive calls.
"""

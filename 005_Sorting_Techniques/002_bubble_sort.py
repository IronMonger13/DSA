"""
INTUITION:
Sort the given array in ascending order using bubble sort.


APPROACH:
Principle - Swap adjacent elements to put the largest element at the last for each iteration. After all iterations, array will be sorted.
Run an outer loop from i=len(arr)-1 to 0.
Run an inner loop from j=0 to i-1.
For each iteration, swap arr[j] and arr[j+1] if arr[j]>arr[j+1].
After each outer iteration, check if any swaps happened, if not, that means array is sorted and break out of the loop.


EDGE CASES:
len(arr) = 0 - return the empty array.
"""


# CODE SOLUTION:
def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        swapped = False

        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = True

        if swapped:
            break

    return arr


arr = [5, 4, 3, 2, 1, 6]
print(bubble_sort(arr))

"""
TIME COMPLEXITY:
O(n^2) - time taken to traverse through the array is O(n), and time taken for each swap iteration is O(n). So total iterations to be performed is O((n-1) + (n-2) + ... + 2), which is O((n(n-1)/2)-1), which simplifies to O(n^2). The best case scenario is O(n) since we iterate the entire array only once and break out since the array given is already sorted.


SPACE COMPLEXITY:
O(1) - no additional data structures were used.


WHY BRUTE FORCE FAILS:
Any input except already sorted array will take O(n^2) time for bubble sort, which is inefficient compared to optimal solutions like merge sort, which sort in O(n log n) time.


WHAT I'D SAY IN AN INTERVIEW:
We have to sort the given array using bubble sort.
We run an outer loop to control till where the inner loop is going to run for each iteration, and in the inner loop, we compare the element to its next element. If the element is larger than the next one, we swap the elements. When the inner loop runs till the end, the largest element moves towards the end, and when all iterations are completed, we get an array sorted in ascending order. We can optimize it to stop the iterations if there are no more swaps happening, meaning the array is now in sorted order.
Time complexity is O(n^2) since we traverse through the array and for each element, compare it to its adjacent element. Best case time complexity is O(n), since we stop after the first iteration since no swaps happened, meaning array is already sorted. Space complexity is O(1) since no additional data structures were used.
"""

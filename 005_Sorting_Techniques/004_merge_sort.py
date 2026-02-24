"""
INTUITION:
Sort the given array in ascending order using merge sort.


APPROACH:
Principle - keep dividing the array into two till each subarray is of only one element, then merge these subarrays in sorted order. This is called divide and conquer approach.
Define a function that takes arr, low, and high as parameters.
Define base case - if low == high, return.
Find the mid point as (low+high)/2.
Recursively call the function to divide the array into subarrays, first from low to mid point and then from mid point + 1 to high. This will divide the array into subarrays of only one element.
Define another function to merge these subarrays in sorted order, which takes arr, low, mid and high as parameters.
Inside the function, set left as low and right as mid+1.
Create an empty temp array.
Loop while low <= mid or while right <= high.
If arr[left] < arr[right], append arr[left] to the array and increment left by 1, else append arr[right] and increment right by 1.
Add loops for the remaining array after the first loop has ended to iterate through the left and right as while left <= mid, append arr[left] and increment left by 1, and while right <= high, append arr[right] and increment right by 1.
Copy values from temp array to original array as arr[i] = temp[i-low] to preserve their positions.



EDGE CASES:
len(arr) = 0 - return empty array.
"""


# CODE SOLUTION:
def merge(arr, low, mid, high):
    left = low
    right = mid + 1

    temp = []

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]


def merge_sort(arr, low, high):
    if low >= high:
        return

    mid = (low + high) // 2

    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr, low, mid, high)

    return arr


arr = [1, 2, 4, 3, 5, 9, 8, 7, 0, 6]
low = 0
high = len(arr) - 1
print(merge_sort(arr, low, high))

"""
TIME COMPLEXITY:
O(n log n) - there are log n levels of recursion, and each recursion performs n operations to sort the array.


SPACE COMPLEXITY:
O(n) - since additional space log n space is used for stack space and additional n space is used for storing array elements in a temp array, so space is O(log n + n), which can be simplified to O(n).


WHY BRUTE FORCE FAILS:
Brute force involves comparing each element to the others in the array, which takes up O(n^2) time. Merge sort is optimal since we can sort the array in O(n log n) time.


WHAT I'D SAY IN AN INTERVIEW:
We have to sort the array in ascending order using merge sort.
This can be done by using divide and conquer approach.
Keep dividing the array into subarrays until each subarray has only one element, then merge these subarrays into bigger subarrays in sorted order till the complete array is sorted.
Time complexity is O(n log n) as there are log n levels of recursions, and each recursion performs n operations. Space complexity is O(n) since additional log n space is required for stack recursive calls, and additional n space is required for storing the sorted elements of the array into a temp array, so total space is O(log n + n), which can be simplified to O(n).
"""

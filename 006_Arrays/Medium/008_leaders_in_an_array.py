"""
INTUITION:
For a given array arr, return an array of all leader elements. Leader elements are elements which are greater than all the elements present on their right till the end.


APPROACH:
We can check from the end of the array if an element is leader by comparing current element to max_element, which is updated with each iteration. So we compare each element to the largest element on its right.
1. Initialise:
    - array with single element: res = [arr[-1]]
    - max_element = arr[-1]
2. Iterate from n-2 to 0.
3. For each iteration, if arr[i] > max_element, append arr[i] to res and update max_element to arr[i].
4. Reverse the res arr to get final output in correct order.


EDGE CASES:
len(arr) = 0 - return empty array.
"""


# CODE SOLUTION:
def leader(arr):
    n = len(arr)

    if n == 0:
        return []

    res = [arr[-1]]
    max_element = arr[-1]

    for i in range(n - 2, -1, -1):
        if arr[i] > max_element:
            res.append(arr[i])
            max_element = arr[i]

    start = 0
    end = len(res) - 1
    while start < end:
        res[start], res[end] = res[end], res[start]
        start += 1
        end -= 1

    return res


arr = [10, 22, 12, 3, 0, 6]
print(leader(arr))


"""
TIME COMPLEXITY:
O(n) - we find all the leader elements in a single array pass, and then reverse the array, which takes O(n/2). So total time is O(n + n/2), which simplifies to O(n).


SPACE COMPLEXITY:
O(n) - we need another array/list to store leader elements, which in worst case can take up n space, meaning all the elements are leader elements.


WHY BRUTE FORCE FAILS:
Brute force involves comparing each element to all of the elements to its right to check if its a leader element or not. This can take O(n^2) time.
Our approach is optimal since we find all the leader elements in a single array pass, taking O(n) time.


WHAT I'D SAY IN AN INTERVIEW:
We are given an array and we have to return another array with all the leader elements. A leader is an element who is greater than all the elements on its right.
The last element will always be a leader element as there is no element to its right. We iterate from second last element and keep track of the max_element with each element that we encounter. If any number is greater than that max_element, we append that number to the list and it becomes the new max_element.
Time complexity is O(n) since we find all the leader elements in a single array pass and then reverse the array. Space complexity is O(n) since we need additional space to store the leader elements.
"""

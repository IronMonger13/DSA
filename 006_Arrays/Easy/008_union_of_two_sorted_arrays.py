"""
INTUITION:
Given two sorted arrays a and b of length n and m, find union of a and b (Union means all unique elements from both a and b in single array).


APPROACH:
1. Initialise an empty array to store unique elements.
2. Set two variables as pointers to 0 for iterating in both arrays (i and j).
3. While i < n and j < m, compare a[i] and b[j], insert smaller, and avoid duplicate by comparing with last inserted element. Increment i and j after comparison as required.
4. For the remaining array elements after the above iterations are complete, first loop while i < n.
5. If a[i] not in arr, append a[i] to array. Increment i by 1 if true or false.
6. Repeat the same for b array.
7. Return the array.


EDGE CASES:
None
"""


# CODE SOLUTION:
class Solution:
    def findUnion(a, b):
        n = len(a)
        m = len(b)

        union_arr = []
        i = 0
        j = 0

        while i < n and j < m:
            if a[i] <= b[j]:
                if len(union_arr) == 0 or a[i] != union_arr[-1]:
                    union_arr.append(a[i])
                i += 1
            elif b[j] < a[i]:
                if len(union_arr) == 0 or b[j] != union_arr[-1]:
                    union_arr.append(b[j])
                j += 1

        while i < n:
            if a[i] != union_arr[-1]:
                union_arr.append(a[i])
            i += 1

        while j < m:
            if b[j] != union_arr[-1]:
                union_arr.append(b[j])
            j += 1

        return union_arr


a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]
print(Solution.findUnion(a, b))


"""
TIME COMPLEXITY:
O(n + m) - we traverse both arrays once using two pointers, each pointer moves at most its respective array length. So total operations are proportional to n + m.


SPACE COMPLEXITY:
O(n + m) - if there is no overlap between arrays, all elements from both arrays are stored in the union array.


WHY BRUTE FORCE FAILS:
Brute force approach would insert all elements from both arrays into a set and then sort the result. Inserting into a set takes O(n + m) time and sorting the resulting unique elements takes O((n + m) log(n + m)) time. Since both arrays are already sorted, we can use the two-pointer merge technique to construct the union in O(n + m) time without any additional sorting.


WHAT I'D SAY IN AN INTERVIEW:
We have to find the union of two given sorted arrays in ascending order.
We use two pointers to iterate through the two arrays and compare to find the smaller element and check if the element is present in the array or not. If not, we push and increment the pointer variable by 1 and again compare. We compare until either of the arrays is exhausted and for the remaining array, just check if element already exists at the last position or not. If not, append the element. When all iterations are complete, we get our union array.
Time complexity is O(n + m) since we are iterating through two arrays independently of each other. Space complexity is O(n + m) in worst case since additional n+m space will be required to store unique elements if all elements are different.
"""

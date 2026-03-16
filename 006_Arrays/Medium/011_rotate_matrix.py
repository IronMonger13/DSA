"""
INTUITION:
Given a n x n matrix, we have to rotate the matrix 90 degrees.
This can be done by first taking transpose of the matrix, and then reversing each row individually.


APPROACH:
1. Iterate from row = 0 to n - 1.
2. For each row iteration, iterate from col = row + 1 to n.
3. Swap matrix[row][col] with matrix[col][row].
This way we get the transpose of the entire matrix while only traversing through the upper triangle of the matrix.
4. Iterate from i = 0 to n, and reverse each row.


EDGE CASES:
None
"""

# CODE SOLUTION:
from typing import List


class Solution:
    def reverse(self, arr):
        start = 0
        end = len(arr) - 1
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for row in range(0, n - 1):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for i in range(0, n):
            self.reverse(matrix[i])


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
Solution().rotate(matrix)
print(matrix)


"""
TIME COMPLEXITY:
O(n^2) - transposing requires traversing upper half of the matrix, which takes O(n * n/2) time, and reversing each row takes another O(n * n/2) time, which simplifies to O(n^2).


SPACE COMPLEXITY:
O(1) - matrix is sorted in place and no additional data structures are used.


WHY BRUTE FORCE FAILS:
Brute force involves storing each row as column and each column as row in the relevant positions in a new matrix, which takes O(n^2) time and O(n^2) space.
This approach is optimal since we rotate the entire matrix by 90 degrees in O(n^2) time and O(1) space as rotation happens in-place.


WHAT I'D SAY IN AN INTERVIEW:
We are given a nxn matrix and we have to rotate the matrix by 90 degrees.
We can do so easily by first taking transpose of the matrix by swapping matrix[row][col] with matrix[col][row], and then reversing each row so the matrix is in correct order.
Time complexity is O(n^2) since we have to iterate through the entire matrix, which takes O(n^2) time, and space complexity is O(1) since matrix rotation happens in-place and no additional data structures are used.
"""

"""
INTUITION:
We are given a matrix and need to traverse it in spiral order.
Spiral traversal means:
- Move left to right across the top row
- Then top to bottom on the right column
- Then right to left across the bottom row
- Then bottom to top on the left column
We repeat this process while shrinking the boundaries of the matrix.


APPROACH:
1. Initialize four pointers:
    - top = 0
    - bottom = m - 1
    - left = 0
    - right = n - 1
2. While top <= bottom and left <= right:
    - Traverse from left to right (top row), then increment top
    - Traverse from top to bottom (right column), then decrement right
    - If top <= bottom, traverse from right to left (bottom row), then decrement bottom
    - If left <= right, traverse from bottom to top (left column), then increment left
3. Continue until all elements are traversed.
4. Store elements in a result list and return it.


EDGE CASES:
1. Empty matrix - return empty list
2. Single row matrix
3. Single column matrix
4. Matrix with one element
"""


# CODE SOLUTION:
class Solution:
    def spiralOrder(self, matrix):
        result = []

        if not matrix:
            return result

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:

            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().spiralOrder(matrix))


"""
TIME COMPLEXITY:
O(m * n) - every element in the matrix is visited exactly once.


SPACE COMPLEXITY:
O(1) - no additional data structures were used. O(n * m) if counting space used to store result.


WHY BRUTE FORCE FAILS:
There is no real brute force alternative here.
Any solution must visit all elements, so O(m * n) is optimal.


WHAT I'D SAY IN AN INTERVIEW:
The problem asks us to traverse a matrix in spiral order, covering all elements exactly once.
We use four pointers (top, bottom, left, right) to define the current boundaries and shrink them after each traversal step.
Time complexity is O(m * n) since every element is visited once, and space complexity is O(1) as no additional data structures were used, or O(n * m) if counting the space used to store the result.
"""

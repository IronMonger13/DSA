"""
INTUITION:
We are given an m x n matrix. If any element in the matrix is 0, we must set its entire row and column to 0.
A naive approach would mark rows and columns separately using extra arrays. However, the problem requires modifying the matrix in-place.
We can use the first row and first column of the matrix as markers to record which rows and columns should be turned into zero.
If matrix[i][j] == 0, we mark:
    - matrix[i][0] = 0  (row marker)
    - matrix[0][j] = 0  (column marker)
Later, using these markers we update the rest of the matrix accordingly.
Since the first column itself is being used as a marker, we maintain a separate variable to track whether the first column originally contained a zero.


APPROACH:
1. Initialize a variable col0 = 1 to track whether the first column should be set to zero.
2. Traverse the matrix:
    - If matrix[i][j] == 0:
        mark the row using matrix[i][0] = 0
        mark the column using matrix[0][j] = 0
    - If matrix[i][0] == 0, update col0 = 0.
3. Traverse the matrix again from bottom-right to top-left:
    - If matrix[i][0] == 0 or matrix[0][j] == 0
        set matrix[i][j] = 0
4. Handle the first column separately using col0.
This ensures we use the matrix itself as storage and avoid additional space.


EDGE CASES:
None
"""


# CODE SOLUTION:
class Solution:
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        col0 = 1

        for i in range(rows):
            if matrix[i][0] == 0:
                col0 = 0

            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

            if col0 == 0:
                matrix[i][0] = 0
        return matrix


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(Solution().setZeroes(matrix))


"""
TIME COMPLEXITY:
O(m * n) - we traverse the matrix twice. Each traversal processes every element once.


SPACE COMPLEXITY:
O(1) - no additional data structures are used. The matrix itself is used for storing markers.


WHY BRUTE FORCE FAILS:
A brute force approach would use two additional arrays:
- row[m]
- col[n]
First we mark which rows and columns contain zero.
Then we traverse again and set those positions to zero.
This approach works but requires O(m + n) extra space.
The optimal approach reduces the extra space to O(1) by using the first row and first column as markers.


WHAT I'D SAY IN AN INTERVIEW:
The straightforward approach is to use two arrays to track which rows and columns should be set to zero, which takes O(m+n) space.
However, we can optimize this by using the first row and first column of the matrix as markers. Whenever we encounter a zero at matrix[i][j], we mark the corresponding row and column by setting matrix[i][0] and matrix[0][j] to zero.
Because the first column is used as a marker, we track it separately using a variable. After marking, we traverse the matrix in reverse order and update elements based on these markers.
This allows us to solve the problem in O(m * n) time and O(1) extra space.
"""

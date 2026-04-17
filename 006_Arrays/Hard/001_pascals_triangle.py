"""
INTUITION:
We need to generate Pascal’s Triangle up to numRows.
Each element in the triangle corresponds to a binomial coefficient (nCr).

Instead of building each row using the previous row, we can directly compute
each element using the formula:
    nCr = nC(r-1) * (n - r + 1) / r

This allows us to generate each row efficiently in O(row) time without using extra space.


APPROACH:
1. For each row from 1 to numRows:
    - Generate that row independently using the nCr formula.
2. To generate a row:
    - Start with first element = 1 (since nC0 = 1).
    - Use the relation:
        next_element = current_element * (row - col) // col
    - Append each computed element to the row.
3. Store each row in the final result list.
4. Return the result.


EDGE CASES:
- numRows = 0 → return empty list
- numRows = 1 → return [[1]]
"""

from typing import List


class Solution:
    def generate_row(self, row):
        curr_element = 1
        temp = [curr_element]

        for col in range(1, row):
            curr_element = (curr_element * (row - col)) // col
            temp.append(curr_element)

        return temp

    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        for row in range(1, numRows + 1):
            ans.append(self.generate_row(row))

        return ans


"""
TIME COMPLEXITY:
O(n^2) - We generate n rows, and each row takes O(row) time.
Total work = 1 + 2 + 3 + ... + n = O(n^2)


SPACE COMPLEXITY:
O(n^2) - We store the entire Pascal’s Triangle.


WHY BRUTE FORCE FAILS:
Brute force approach would compute nCr using factorials:
    n! / (r! * (n-r)!)
This is inefficient because:
- Factorial computation is costly
- Repeated calculations lead to redundant work
- Risk of overflow for large values

The optimal approach uses iterative relation to compute each element in O(1),
avoiding repeated factorial computations.


WHAT I'D SAY IN AN INTERVIEW:
We are asked to generate Pascal’s Triangle up to numRows.
Each element in the triangle is a binomial coefficient.

Instead of using factorials, we use an iterative formula to compute each element
in constant time from the previous one:
    next = current * (row - col) // col

We generate each row independently using this relation and append it to the result.

Time complexity is O(n^2) since we generate all rows, and space complexity is
O(n^2) to store the triangle.
"""

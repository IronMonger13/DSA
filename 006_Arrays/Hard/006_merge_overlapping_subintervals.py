"""
INTUITION:
Given an array of intervals with a start and end value, we have to merge all the overlapping intervals. For example, if one interval is [2,5] and another is [3,9], then the overlapped interval would be [2,9]. This means that the first element of an interval should lie between the elements of another interval for them to overlap.
We are also given the constraints that-
1. 1 <= intervals.length <= 104
2. intervals[i].length == 2
3. 0 <= starti <= endi <= 104, starti and endi are the start and end intervals.


APPROACH:
1. Initialise an empty array to store the overlapped intervals (ans).
2. Sort the array so that we can find the overlapping intervals in a single array pass.
3. If ans is empty or the intervals lower element is greater than the upper element stored latest in ans, then that means current interval doesnt overlap and we need to create a new interval, so we append the current interval to ans.
4. Else, meaning the first element of the current interval lies between the lower and upper elements of the last interval stored in ans. So we just find the max of the upper elements from current interval and last interval stored in ans. We dont need to find the min since they are already in sorted order, so lower element will always be the minimum value.
5. Return ans.


EDGE CASES:
Due, to constraints, there wont be any edge cases that wont be handled by general solution.
"""

# CODE SOLUTION:
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        ans = []
        intervals.sort()

        for i in range(0, n):
            if not ans or intervals[i][0] > ans[-1][-1]:
                ans.append(intervals[i])
            else:
                ans[-1][-1] = max(ans[-1][-1], intervals[i][1])

        return ans


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(Solution().merge(intervals))


"""
TIME COMPLEXITY:
O(n log n) - all the overlapping intervals were found in a single array pass (O(n)), but the array was sorted before to achieve the result, so total time complexity becomes (O(n log n) + O(n)), which simplifies to O(n log n).


SPACE COMPLEXITY:
O(n) - additional space is required to store the overlapping intervals.


WHY BRUTE FORCE FAILS:
Brute force includes checking each interval with another one to find if they overlap, which can take up O(n^2) time.
This approach is optimal since we find the overlapping subintervals in O(n log n) time by sorting and then finding the overlapping subintervals in a single array pass, which takes O(n log n) time ans O(n) space in the worst case.


WHAT I'D SAY IN AN INTERVIEW:
We are given a list of intervals and need to merge all overlapping ones.
First, I sort the intervals based on start time so overlapping intervals come next to each other.
Then I iterate through the intervals:
- If the current interval does not overlap with the last merged interval (current_start > last_end), I add it as a new interval.
- Otherwise, I merge them by updating the end of the last interval to max(last_end, current_end).
Since the array is sorted, we don’t need to worry about updating the start.
Time complexity is O(n log n) due to sorting, and space complexity is O(n) for the result.
"""

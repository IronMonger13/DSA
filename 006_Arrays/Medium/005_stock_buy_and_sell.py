"""
INTUITION:
We are given an array called prices, where price of stock is prices[i] on ith day. We have to find what can be the maximum profit we can make after buying and selling stock. We can only sell after we have bought the stock.


APPROACH:
We can keep a track of max_profit from all the profits and lowest price of the share for ith day. So profit for ith day will be stock price on day i - min value before i index. Keep a track of the max profit.
1. Initialise:
    - max_profit = 0
    - min_price = prices[0]
2. Loop from i = 1 to len(prices)-1.
3. Calculate profit for each day and store the max profit in max_profit.
4. Update the min_price by comparing previous min price and current price.


EDGE CASES:
None
"""

# CODE SOLUTION:
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        min_price = prices[0]

        for i in range(1, n):
            profit = prices[i] - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, prices[i])

        return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))


"""
TIME COMPLEXITY:
O(n) - we find the max_profit in a single array pass.


SPACE COMPLEXITY:
O(1) - no additional space or data structures were used.


WHY BRUTE FORCE FAILS:
Brute force involves checking sum for all different days, so we check for buying on first day and selling on second, then third, and so on. This will take O(n^2) time since we are iterating n-i times for every i.
This approach is optimal since we keep track of the min element before ith day, and calculate profit only using the min_price, which allows us to calculate max profit in a single array pass, hence taking only O(n) time.


WHAT I'D SAY IN AN INTERVIEW:
We are given an array called prices where each element is the price of a stock on ith day. We have to find what is the maximum profit we can make.
We keep a track of the max profit recorded and min price found to buy the stock till ith day. We calculate profit and compare it to max_profit to keep the max value, and then compare current price to min_price to update the min_price value.
Time complexity is O(n) since we find the max profit in a single array pass. Space complexity is O(1) since no additional data structures or space was used.
"""

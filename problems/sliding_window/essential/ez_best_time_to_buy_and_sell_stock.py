from typing import List

class BestTimeToBuyAndSellStock:
    """
    LeetCode Question Nr.121
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    Input: prices = [7,1,5,3,6,4]  Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

    Input: prices = [7,6,4,3,1]  Output: 0
    """

    @staticmethod
    def great_ans1(prices: List[int]) -> int:
        """
        tech use : sliding window
        Time: O(nlogn)
        Memory: O(1)
        https://www.youtube.com/watch?v=1pkOgXD63yU

        my note: we can directly skip current-run loop when T+1-day price lower than T-day one because this guarantee that:
        1. no profit from buy at T and sell at T+1 
        2. even there is higher price in nth-day, we can still skip this round directly 
           because (t+N-day - T+1-day) will always greater than (T+N-day - T-day)
        """
        l, r = 0, 1
        max_p = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                max_p = max(prices[r] - prices[l], max_p)
            else:
                l = r   # shift to new lowest point 
            
            r += 1

        return max_p   
    

    @staticmethod
    def my_solution1(prices: List[int]) -> int:
        """
        This is OVERTIME solution:
        Time: O(n^2) : python max/min will contribute O(n) and the outer loop also contribute O(n)
        """
        max_profit = 0 
        for i in range(len(prices)-1):
            profit = max(prices[i:]) - prices[i]
            if profit > max_profit:
                max_profit = profit
        return max_profit

    
    @staticmethod
    def my_solution1(prices: List[int]) -> int:
        """
        This is OVERTIME solution:
        Time: O(n^2) : python max/min will contribute O(n) and the outer loop also contribute O(n)
        """
        if len(prices) <= 1:
            return 0

        l, r = 0, 1
        max_p = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                r2 = r
                while r2 < len(prices):
                    profit = prices[r2] - prices[l]
                    if profit > max_p:
                        max_p = profit
                    r2 += 1

            l, r = l+1, r+1 

        return max_p   

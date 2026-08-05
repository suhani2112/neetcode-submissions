class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i =0
        profit = 0
        n = len(prices)
        for j in range(i+1 , n):
            if prices[i] < prices[j]:
                profit += prices[j] - prices[i]
                i += 1
                j += 1
            else:
                i += 1
                j += 1
        return profit 
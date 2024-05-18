class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=len(prices)
        mincost = float('inf')
        maxProfit = 0

        while l<r:
            profit = prices[l]-mincost
            if profit>maxProfit:
                maxProfit=profit
                
            if prices[l]<mincost:
                mincost=prices[l]
            l+=1

        return maxProfit
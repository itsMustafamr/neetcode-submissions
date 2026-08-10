class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #way - best - sliding window using 2 pointer
        # l, r = 0, 1 #left - buy, right - sell
        # maxP = 0

        # while r < len(prices):
        #     #profitable ?
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         maxP = max(maxP, profit)
        #     else:
        #         l = r
        #     r += 1
        # return maxP
        #way 2 - brut force
    #     class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     res = 0
    #     for i in range(len(prices)):
    #         buy = prices[i]
    #         for j in range(i + 1, len(prices)):
    #             sell  = prices[j]
    #             res = max(res, sell - buy)
    #     return res

        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l] 
                maxP = max(maxP, profit)
            
            else:
                l = r
            r += 1
        return maxP





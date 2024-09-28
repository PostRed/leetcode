class Solution:
    def maxProfit(self, prices):
        min_p = 1e9
        ans = 0
        for i in range(len(prices)):
            # максимизируем разницу между текущей стоимостью и минимальной
            ans = max(ans, prices[i] - min_p)
            if prices[i] < min_p:
                min_p = prices[i]
        return ans

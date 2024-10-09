class Solution:
    def numSquares(self, n):
        # хранение минимального количества квадратов для каждого числа от 0 до n
        dp = [1e9] * (n + 1)
        dp[0] = 0
        for i in range(n + 1):
            # для каждого числа перебираем все совершенные квадраты
            for j in range(1, int(i ** 0.5) + 1):
                dp[i] = min(dp[i], dp[i - j ** 2] + 1)
        return dp[n]

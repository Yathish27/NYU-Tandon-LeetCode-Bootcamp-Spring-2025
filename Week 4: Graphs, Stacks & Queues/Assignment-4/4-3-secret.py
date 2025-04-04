class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 1000000007
        dp = [0] * (n + 1)
        dp[1] = 1
        sharing_today = 0
        
        for day in range(1, n + 1):
            if day >= delay:
                sharing_today = (sharing_today + dp[day - delay + 1]) % MOD
            if day >= forget:
                sharing_today = (sharing_today - dp[day - forget + 1]) % MOD
            if day < n:
                dp[day + 1] = sharing_today
        total = 0
        for i in range(max(1, n - forget + 1), n + 1):
            total = (total + dp[i]) % MOD
        return total

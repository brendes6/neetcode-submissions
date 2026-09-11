class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0 for _ in range(amount+1)]
        dp[0] = 1

        for c in coins:
            for i in range(amount+1):
                if c <= i:
                    dp[i] += dp[i-c]
        
        return dp[-1]
        
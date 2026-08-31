class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        2d DP solution. The main state is the amount of profit that we have,
        and the second state is whether we are in cooldown or not. Thus, it is a
        2d array where the length of main array is 2. dp[i][c] represents
        the max amount of profit we can have on day i, with cooldown on/off of c.

        Approach: run DFS with memoization. We have two states: index in prices,
        and whether we are currently holding. If we are currently holding,
        we have the choice of either selling (and recursing 2 spots ahead) and increasing profit or skipping forward.
        If we aren't holding, we have the choice of buying or skipping forward. These results all depend on the
        future result, and to prevent re-calculating the same val multiple times we memoize.

        """

        dp = [[None for _ in range(2)] for _ in range(len(prices))]

        def dfs(i, holding):
            if i >= len(prices):
                return 0

            if dp[i][holding]:
                return dp[i][holding]
            
            
            if holding == 1:
                # sell or skip
                res = max(
                    prices[i] + dfs(i+2, 0),
                    dfs(i+1, holding)
                )
                dp[i][holding] = res
                return res
            else:
                # buy or skip
                res = max(
                    -prices[i] + dfs(i+1, 1),
                    dfs(i+1, holding)
                )
                dp[i][holding] = res
                return res

        
        return dfs(0, 0)





        
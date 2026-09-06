class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        """
        Approach: Longest increasing subsewuence. We need to determine the length
        of the longest strictly increasing subsequence. I think this has a DP approach but 
        I'm not sure.

        So this is a DP approach, but it is more of a memoization approach than
        iterating an array. We have two state parameters we want to memoize by:
        which index we are at in nums, and what the length of the current longest
        subsequence is. Since second one is max N, n*n memoization grid will be used

        """
        n = len(nums)


        dp = [[None for _ in range(n)] for _ in range(n)]

        # cur ind, cur lis len, prev added
        def recur(i, j):
            if i == n:
                return 0

            if j >= 0 and dp[i][j]:
                return dp[i][j]
            
            if j==-1 or nums[i] > nums[j]:
                val = max(1 + recur(i+1, i), recur(i+1, j))
            else:
                val = recur(i+1, j)
            
            dp[i][j] = val
            return val
        
        return recur(0, -1)
            

        
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


        dp = [1 for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)
            

        
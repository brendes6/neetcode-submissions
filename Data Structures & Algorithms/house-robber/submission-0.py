class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Strategy: this is a DP problem. Each position we have a certain choice:
        rob a house and keep the money from it AND the amt of money we would have had from 
        robbing up to the 2nd prev house, or skip and carry on the amount of money
        we had at the house before. THe state is simply how much money we have at 
        a specific position. At each new position, the state depends on which option we deem
        to be more valuable, which is dependent on past decisions.

        Thus, we maintain a prev1 and prev2 var, where prev1 is the max amt of money 
        we could have gotten up to the previous house, and prev2 is the max amt of money
        we could have gotten up to the 2nd previous house. The best choice at any house
        is the max of the prev and old prev, and we update this house's state with that.

        """

        prev1, prev2 = 0, 0
        dp = [0 for _ in range(len(nums))] # state: max profit achievable at each house


        for i, n in enumerate(nums):
            cur = max(prev1, prev2 + n)
            dp[i] = cur
            prev1, prev2 = cur, prev1
        
        return dp[-1]


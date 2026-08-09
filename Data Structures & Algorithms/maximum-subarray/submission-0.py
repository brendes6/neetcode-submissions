class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        """
        Approach: we can simply choose whether to include a part of the array
        if its running sum is > 0. if we reach ad val that makes the array go negative,
        we record this running sum, and reset it to 0.

        """

        running_sum, most = 0, float('-inf')

        for num in nums:
            running_sum += num
            if running_sum > most:
                most = running_sum
            if running_sum < 0:
                running_sum = 0
        
        return most

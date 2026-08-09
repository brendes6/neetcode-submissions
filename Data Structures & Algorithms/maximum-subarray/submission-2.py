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


        """
        Postmortem: This is one of those DP problems that initially seems
        tough when you view it as a sliding window problem. looking at it
        as a sliding window problem, you immediately realize it's impossible to know
        whether adding a val is good or bad or expanding bc you don't know upcoming vals.

        The approach requires a dp approach where you realize that if the current
        subarray sum is > 0, we obv want to include it in including calculations. Once the sum becomes less than
        zero, it's dead weight and we drop it. calculating max every iteration is fine since its guarenteed
        to only be n comparisions.
        """

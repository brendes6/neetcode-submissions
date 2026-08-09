class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        strategy: prefix/postfix array. at every index, we want to have
        an array showing the products of values up until that point, which
        we can multiply to get the value for each spot in array.
        """

        n = len(nums)

        prefix, postfix = [1] * n, [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
            postfix[i] = postfix[i-1] * nums[n - i]
        
        postfix.reverse()
        
        ret = [1] * n
        # print(prefix, postfix)

        for j in range(n):
            ret[j] = prefix[j] * postfix[j]
        
        return ret

"""
Postmortem: I feel like every time I solve this one I do it a little
bit different, but this one worked out well. The strategy is just to align
the prefix and postfix arrays such that when I index them at a common
point, it represents the product of values up until + after a point.
"""
        
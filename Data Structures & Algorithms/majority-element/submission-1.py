class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict

        div = len(nums) / 2
        
        d = defaultdict(int)

        for n in nums:
            d[n] += 1
            if d[n] >= div:
                return n
                


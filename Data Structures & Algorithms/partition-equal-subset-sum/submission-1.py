class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 != 0:
            return False
        
        val = sum(nums) // 2

        nums.sort(reverse=True)

        stack = []

        self.works = False
        self.memo = {}

        def backtrack(i, p1, p2, val):
            if i >= len(nums):
                if p1 == p2 == val:
                    self.works = True
                return
            
            if i==0:
                backtrack(i+1, p1 + nums[i], p2, val)
            else:
                if p1 + nums[i] <= val:
                    backtrack(i+1, p1 + nums[i], p2, val)
                    if self.works:
                        return
                
                if p2 + nums[i] <= val:
                    if self.works:
                        return
                    backtrack(i+1, p1, p2 + nums[i], val)
        
        backtrack(0, 0, 0, val)
        return self.works
                    

        
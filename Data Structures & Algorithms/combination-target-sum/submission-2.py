class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Strategy: backtracking approach using a stack to
        track current state of combinations. Since we can
        repeat numbers but order of numbers doesn't matter,
        we want to recurse on all vals ahead of a num
        including itself.
        """

        results = []

        stack = []
        
        def backtrack(nums, i):
            # if stack is match or too large, return
            if sum(stack) == target:
                results.append(stack.copy())
                return
            if sum(stack) > target:
                return
            

            for j in range(i, len(nums)):
                stack.append(nums[j])
                backtrack(nums, j)
                stack.pop()
        
        backtrack(nums, 0)
        return results
            


        
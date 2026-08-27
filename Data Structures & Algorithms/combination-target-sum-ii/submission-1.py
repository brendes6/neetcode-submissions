class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # same as 1 but dont consider current index as candidate?

        # [1, 2, 2, 4, 5, 6, 9]


        results = []

        stack = []

        def backtrack(nums, i, cur_sum):
            if cur_sum==target:
                results.append(stack.copy())
                return
            if cur_sum > target:
                return
            if i >= len(nums):
                return
            

            for j in range(i, len(nums)):
                # Some condition here to prevent recursing on duplicate elements,
                # BUT we still want to use them together. e.g. using 2 and 2 in the SAME
                # stack, but not making seperate stacks like [2], [2] or [1,2], [1, 2]

                if j > i and nums[j] == nums[j-1]:
                    continue
            
                stack.append(nums[j])
                cur_sum += nums[j]
                backtrack(nums, j+1, cur_sum)
                stack.pop()
                cur_sum -= nums[j]
        
        backtrack(sorted(candidates), 0, 0)
        return results
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """ Subsets
        Ok so its obviously backtracking but I think its easy with a 
        stack based approach. so the decision tree is that on every
        new letter, we continue either with vs without adding it.
         Thus, if we maintain a stack as a global variable and in the
         recursion run 1. recurse 2. add val to stack 3. recurse again
         then we can successfully run it with vs without the num

        """


        stack = []
        vals = []

        def recur(nums, i):
            if i==len(nums):
                vals.append(stack.copy())
                return
            
            recur(nums, i+1)
            stack.append(nums[i])
            recur(nums, i+1)
            stack.pop()
        
        recur(nums, 0)

        return vals
            

            
        
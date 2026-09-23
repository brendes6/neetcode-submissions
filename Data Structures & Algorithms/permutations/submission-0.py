class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        backtracking permutations approach:

        run backtrack tracking state of list in stack

        run dfs(i). at index i, check if any nums are not
        currently in use. for each one, add to stack and seen,
        recur, and remove from stack and seen

        """


        stack = []
        seen = set()
        ret = []


        def dfs(i, n):
            # if we reach end of list, we have valid perm to add
            if i==n:
                ret.append(stack.copy())
        
            # for any number not currently in stack,
            # add at this index, recur, then remove

            for ind in range(0, n):
                if ind not in seen:
                    seen.add(ind)
                    stack.append(nums[ind])
                    dfs(i+1, n)
                    seen.remove(ind)
                    stack.pop()
                
        dfs(0, len(nums))

        return ret
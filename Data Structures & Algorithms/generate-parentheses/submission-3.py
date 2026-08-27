class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        """
        Backtracking approach, where we
        decide to add l or r parenthesis, while doing early pruning of invalid solutions
        based on whether l < r.
        """


        sols = []

        stack = []

        def backtrack(l, r, n):
            if l==r==n:
                sols.append("".join(stack))
                return
            
            # Only time we can add a right
            if l > r:
                stack.append(")")
                backtrack(l, r+1, n)
                stack.pop()
                
            if l < n:
                stack.append("(")
                backtrack(l+1, r, n)
                stack.pop()
        
        backtrack(0, 0, n)
        return sols

            


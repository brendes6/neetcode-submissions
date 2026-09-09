class Solution:

    def queenString(self, stack, n):
        ret = [["." for _ in range(n)] for _ in range(n)]

        for r, c in stack:
            ret[r][c] = "Q"
        
        return ["".join(val for val in lst) for lst in ret]

        
    
    def works(self, stack, x, y):
        if not stack:
            return True
        
        for r, c in stack:
            if r==x or c==y or (r-c == x-y) or (r+c == x+y):
                return False
        
        return True
    

    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Approach: backtracking. We iterate on a simple rule: we can 
        only place one queen on each row, col, diag. We then backtrack
        while iterating rows, testing different combinations of placing
        queens. We have a stack up to size n, where we check
        whether placing a new queen on a new spot would work. if it works,
        explore backtracked choice.
        """



        res = []

        stack = []
        
        def backtrack(i):
            if i==n:
                res.append(self.queenString(stack, n))
                return

            for j in range(n):
                if self.works(stack, i, j):
                    stack.append((i, j))
                    backtrack(i+1)
                    stack.pop()
        
        backtrack(0)
        return res



        
class Solution:


        
    
    

    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Approach: backtracking. We iterate on a simple rule: we can 
        only place one queen on each row, col, diag. We then backtrack
        while iterating rows, testing different combinations of placing
        queens. We have a stack up to size n, where we check
        whether placing a new queen on a new spot would work. if it works,
        explore backtracked choice.
        """

        ret = [["." for _ in range(n)] for _ in range(n)]

        

        res = []

        stack = []
        colS = set()
        diagS1 = set()
        diagS2 = set()
        
        def backtrack(i):
            if i==n:
                res.append(["".join(val for val in lst) for lst in ret])
                return

            for j in range(n):
                if j not in colS and (i-j) not in diagS1 and (i+j) not in diagS2:
                    stack.append((i, j))
                    colS.add(j)
                    diagS1.add(i-j)
                    diagS2.add(i+j)
                    ret[i][j] = "Q"

                    backtrack(i+1)
                    stack.pop()
                    colS.remove(j)
                    diagS1.remove(i-j)
                    diagS2.remove(i+j)
                    ret[i][j] = "."
        
        backtrack(0)
        return res



        
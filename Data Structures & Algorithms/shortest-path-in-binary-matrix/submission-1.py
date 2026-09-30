class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Obviously using BFS, we start from top left and 
        add all right/down/diag neighbors that are 0
        
        keep going until queue is empty, if so return -1,
        else when we reach (n-1, n-1), we return the amount of turns it took to reach.

        """

        if grid[0][0] == 1:
            return -1

        from collections import deque
        
        n = len(grid) - 1

        q = deque([(0, 0, 1)])
        seen = set()


        while q:
            x, y, pth = q.popleft()
            if (x, y) in seen:
                continue

            seen.add((x, y))

            if x==y==n:
                return pth
            
            if x+1 <= n and (x+1, y) not in seen and grid[x+1][y]==0:
                q.append((x+1, y, pth+1))
            
            if y+1 <= n and (x, y+1) not in seen and grid[x][y+1]==0:
                q.append((x, y+1, pth+1))
            
            if x+1 <= n and y+1 <= n and (x+1, y) not in seen and grid[x+1][y+1]==0:
                q.append((x+1, y+1, pth+1))
            
        return -1



        
        
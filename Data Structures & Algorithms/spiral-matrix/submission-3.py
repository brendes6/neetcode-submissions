class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Logic behind moving: start moving right. Any time the next
        # space to move to is either out of bounds OR already seen,
        # transition.

        def in_range(x, y, m, n):
            if not (0 <= x < m) or not (0 <= y < n):
                return False
            return True


        transitions = {(0, 1):(1, 0), (1,0):(0, -1), (0,-1):(-1,0), (-1,0):(0,1)}

        seen = set()
        m, n = len(matrix), len(matrix[0])

        cur = (0, 0)
        move = (0, 1)
        ret = []

        while cur not in seen:

            if len(seen)==m*n:
                return ret
            
            if not in_range(cur[0]+move[0], cur[1]+move[1], m, n) or (cur[0]+move[0], cur[1]+move[1]) in seen:
                move = transitions[move]

            seen.add(cur)
            ret.append(matrix[cur[0]][cur[1]])
            cur = (cur[0]+move[0], cur[1]+move[1])
        
        return ret

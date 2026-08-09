class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Strategy: I think the naive approach would obv be to check for dupes in
        every row, column, and box. Ok actually that is the solution lol
        """

        # maintain one set to track row, col, box and j clear
        cur_set = set()
        for row in board:
            for val in row:
                if val != ".":
                    if val in cur_set:
                        return False
                    cur_set.add(val)
        
            cur_set.clear()
        
        for i in range(len(board)):
            for j in range(len(board)):
                val = board[j][i]
                if val != ".":
                    if val in cur_set:
                        return False
                    cur_set.add(val)
        
            cur_set.clear()
        
        boxes = [set() for i in range(len(board))]
        for r in range(len(board)):
            for c in range(len(board)):

                val = board[r][c]
                box_ind = (r // 3) * 3 + (c // 3)
                if val != ".":
                    if val in boxes[box_ind]:
                        return False
                    boxes[box_ind].add(val)
        
        return True

        """
        Postmortem: This one is a bit akward. But we just need to iterate
        each row and col, checking for duplicates. The approach to make multiple
        box sets and index at a specific one worked. Time wise it can beat all other solutions,
        but looking at memory, this isn't the fastest memory approach though
        """


        
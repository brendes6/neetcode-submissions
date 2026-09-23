class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Similar approach to word search II, but we don't need a 
        trie since there is only one word. Thus, on each dfs traversal,
        we store the index of the word we are currently searching for.

        """

        self.res = False
        seen = set()

        def dfs(i, j, m, n, word_ind):
            seen.add((i, j))
            if word_ind == len(word):
                self.res = True
                return 
            
            if i-1 >= 0 and board[i-1][j] == word[word_ind] and (i-1, j) not in seen:
                dfs(i-1, j, m, n, word_ind+1)
            
            if i+1 < m and board[i+1][j] == word[word_ind] and (i+1, j) not in seen:
                dfs(i+1, j, m, n, word_ind+1)
                
            if j-1 >= 0 and board[i][j-1] == word[word_ind] and (i, j-1) not in seen:
                dfs(i, j-1, m, n, word_ind+1)
            
            if j+1 < n and board[i][j+1] == word[word_ind] and (i, j+1) not in seen:
                dfs(i, j+1, m, n, word_ind+1)
            
            seen.remove((i, j))

        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    dfs(i, j, m, n, 1)
                    if self.res:
                        return True
        
        return self.res
        
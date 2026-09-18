
"""
Prefix tree solution: we need to implement a trie that
stores words and allows us to search whether
a certian string of chars is a prefix of an existing
work in the trie.

"""

class TrieNode:
    def __init__(self, val=None, is_end=False):
        self.val = val
        self.isEnd = is_end
        self.children = {}
    
    def add_child(self, child, node):
        self.children[child] = node
    
    def get_child(self, child):
        return self.children[child]
    
    def has_child(self, child):
        return child in self.children
    
    def make_end(self):
        self.isEnd = True
    
    def is_end(self):
        return self.isEnd

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root

        for i in range(len(word)):
            c = word[i]

            if cur.has_child(c):
                temp = cur.get_child(c)
            else:
                temp = TrieNode(val=c)
                cur.add_child(c, temp)
            
            if i == len(word)-1:
                temp.make_end()
            
            cur = temp


    def search(self, prefix):
        cur = self.root

        for i in range(len(prefix)):
            c = prefix[i]

            if cur.has_child(c):
                temp = cur.get_child(c)
            else:
                return False
            
            cur = temp
        
        return True
    
    def inTree(self, word):
        cur = self.root

        for i in range(len(word)):
            c = word[i]

            if cur.has_child(c):
                temp = cur.get_child(c)
            else:
                return False
            
            cur = temp
        
        return cur.is_end()


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    

        # Create and populate trie, run search on each
        # val in board, only proceding to vals with valid searches

        tree = Trie()

        self.max_moves = 0

        for word in words:
            tree.insert(word)
            self.max_moves = max(self.max_moves, len(word))
        

        self.found_words = set()
        self.cur_path = set()
        
        def dfs(i, j, m, n, moves, curWord):
            if tree.inTree(curWord):
                # print(i, j, curWord)
                self.found_words.add(curWord)
            
            if moves > self.max_moves:
                return
            # else:
            #     print(i, j, curWord, self.cur_path)
            
            if i > 0:
                if (i-1, j) not in self.cur_path and tree.search(curWord + board[i-1][j]):
                    self.cur_path.add((i-1, j))
                    dfs(i-1, j, m, n, moves + 1, curWord + board[i-1][j])
                    self.cur_path.remove((i-1, j))
            
            if i < m-1:
                if (i+1, j) not in self.cur_path and tree.search(curWord + board[i+1][j]):
                    self.cur_path.add((i+1, j))
                    dfs(i+1, j, m, n, moves + 1, curWord + board[i+1][j])
                    self.cur_path.remove((i+1, j))
            
            if j > 0:
                if (i, j-1) not in self.cur_path and tree.search(curWord + board[i][j-1]):
                    self.cur_path.add((i, j-1))
                    dfs(i, j-1, m, n, moves + 1, curWord + board[i][j-1])
                    self.cur_path.remove((i, j-1))
            
            if j < n-1:
                if (i, j+1) not in self.cur_path and tree.search(curWord + board[i][j+1]):
                    self.cur_path.add((i, j+1))
                    dfs(i, j+1, m, n, moves + 1, curWord + board[i][j+1])
                    self.cur_path.remove((i, j+1))
                

        m, n = len(board), len(board[0])
        

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.cur_path.add((i, j))
                dfs(i, j, m, n, 0, board[i][j])
                self.cur_path.remove((i, j))
        
        return list(self.found_words)














        
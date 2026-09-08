class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        
        cur_node = self.root

        for i in range(len(word)):
            if word[i] in cur_node.children:
                nxt = cur_node.children[word[i]]
            else:
                nxt = TrieNode()
                cur_node.children[word[i]] = nxt
            
            if i == len(word) - 1:
                nxt.isEnd = True
            else:
                cur_node = nxt


    def search(self, word: str) -> bool:
        cur_node = self.root

        for i in range(len(word)):
            if word[i] not in cur_node.children:
                return False
            
            nxt = cur_node.children[word[i]]
            
            if i == len(word) - 1:
                return nxt.isEnd
            else:
                cur_node = nxt
        

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root

        for i in range(len(prefix)):
            if prefix[i] not in cur_node.children:
                return False
            
            nxt = cur_node.children[prefix[i]]
            
            cur_node = nxt
        
        return True
        
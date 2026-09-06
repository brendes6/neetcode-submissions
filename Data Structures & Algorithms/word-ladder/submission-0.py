class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        """
        Approach: so this problem seems like it could be solved by constructing
        some sort of graph and running a BFS on it. We want to get the shortest
        path from our source word to the end word, where all traversals are of the same
        weight and a word can traverse to another word if only 1 char is different.

        Thus, we need to form this graph by simply doing a O(n^2) comparison of
        all words including the beginWord and all wordsin wordList. We can define a
        helper function that compares words char by char, ensuring only 1 is diff.

        Once the graph is formed, we start with our source word and BFS on
        all neighbors, tracking the length of the path. Once we reach the endWord,
        we return the shortest path. If we dont reach it, we have a fallback return val
        of 0.

        """
        from collections import deque

        if endWord not in wordList:
            return 0


        def helper(w1, w2):
            retries = 1
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    retries -= 1
                    if retries < 0:
                        return False
            
            return retries==0
        


        # form graph

        graph = defaultdict(list)
        wordList.append(beginWord)

        for i in range(len(wordList)):

            for j in range(i+1, len(wordList)):
                if helper(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        
        q = deque([(beginWord, 1)])
        res = 0
        seen = set()
        seen.add(beginWord)

        while q:

            word, l = q.popleft()
            if word==endWord:
                return l

            for n in graph[word]:
                if n in seen:
                    continue

                seen.add(n)
                q.append((n, l+1))
            

        return res


        







        
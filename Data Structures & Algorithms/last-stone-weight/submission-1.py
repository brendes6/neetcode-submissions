class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        import heapq

        heap = [-s for s in stones]

        heapq.heapify(heap)


        while len(heap) > 1:
            s1, s2 = heapq.heappop(heap), heapq.heappop(heap)

            if s1==s2:
                continue
            
            heapq.heappush(heap, s1-s2)
        
        if len(heap) == 0:
            return 0
        
        return -heap[0]
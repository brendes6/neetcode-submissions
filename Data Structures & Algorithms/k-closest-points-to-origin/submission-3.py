class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """ Strategy: this is a simple heap question. What we need to do is as
        points come in, we calculate it's distance from the origin, and simply
        place it in the queue. then, pop the k least values from the heap

        """
        import math

        def distance(x, y):
            return math.sqrt((x)**2 + (y)**2)


        vals = []

        for x, y in points:
            d = -distance(x, y)
            heapq.heappush(vals, [d, x, y])
            if len(vals) > k:
                heapq.heappop(vals)
        
        ret = []
        for i in range(k):
            d, x, y = heapq.heappop(vals)
            ret.append([x, y])
        
        return ret
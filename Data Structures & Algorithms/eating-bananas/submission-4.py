class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        """
        Make a helper to determine whether
        we can eat bananas in time for a given k, h, bananas.

        Then, in main, run a binary search across all k values (from 1 to max(piles))

        If fails, move right
        if succeeds, move left and include

        """


        def eats(piles, k, h):
            time = 0
            
            for p in piles:
                time += math.ceil(p/k)
            
            return time <= h
        
        l, r = 1, max(piles)

        works = -1

        while l <= r:
            m = (l+r) // 2

            if eats(piles, m, h):
                works = m
                r = m-1
            else:
                l = m+1
        
        return works
        
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """ Strategy: this is a simple heap question. What we need to do is as
        points come in, we calculate it's distance from the origin, and simply
        place it in the queue. then, pop the k least values from the heap

        """
        import math

        def distance(x, y):
            return math.sqrt((x)**2 + (y)**2)


        nums = sorted([(distance(x, y), x, y) for x, y in points], key=lambda x: x[0])

        return [[val[1], val[2]] for val in nums[:k]]
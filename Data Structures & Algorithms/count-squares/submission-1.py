"""
Approach: any time we want to add a point,
we check every other point in the same COLUMN
as the one we are querying (except duplicates at query pnt)

For each point in same column, check diag and row-wise points
that would need to exist. If we have points both at the diag and
row spot, increment answer by the product of number of points at those values

"""

from collections import defaultdict

class CountSquares:

    def __init__(self):
        # map a tuple to num of points there
        self.points = defaultdict(int)
        # map a column to a list of points
        self.diag1 = defaultdict(list)
        self.diag2 = defaultdict(list)
        

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] += 1

        self.diag1[point[0]-point[1]].append(point)
        self.diag2[point[0]+point[1]].append(point)
        

    def count(self, point: List[int]) -> int:
        """
        Given a point x, y:
        search all points i, j on both diagonals
        if [i, y] and [x, j] exist, increment result by
        their product.
        
        """

        x, y = point
        total = 0

        for i, j in self.diag1[x-y] + self.diag2[x+y]:
            if (i, j) != (x, y):
                total += self.points[(i, y)] * self.points[(x, j)]
        
        return total
        

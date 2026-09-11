"""
APproach: using a min heap and a max heap to maintain elements
make sure that diff between min and max heap size is at most 1.
First, add the val to the m


[1, 2, 3, 4, 5, 123, 5435, 5636, 355354,]

min heap managing largest half, max heap managing
smallest half

if val is greater than top heap min, add it there, else
add it to bottom heap.

if one is >1 bigger than the other, pop and add to it
"""
import heapq



class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.minSize = 0
        self.maxSize = 0

        

    def addNum(self, num: int) -> None:
        if not self.minHeap:
            heapq.heappush(self.minHeap, num)
            self.minSize += 1
            return
        
        if num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
            self.minSize += 1
        else:
            heapq.heappush_max(self.maxHeap, num)
            self.maxSize += 1
        
        if self.maxSize > self.minSize + 1:
            val = heapq.heappop_max(self.maxHeap)
            heapq.heappush(self.minHeap, val)
            self.minSize += 1
            self.maxSize -= 1
        
        elif self.minSize > self.maxSize + 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush_max(self.maxHeap, val)
            self.minSize -= 1
            self.maxSize += 1

        

    def findMedian(self) -> float:
        if self.minSize > self.maxSize:
            return self.minHeap[0]
        elif self.maxSize > self.minSize:
            return self.maxHeap[0]
        else:
            return (self.maxHeap[0] + self.minHeap[0]) / 2
        
        
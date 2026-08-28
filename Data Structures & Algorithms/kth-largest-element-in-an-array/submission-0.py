class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use a min heap

        import heapq
        heap = []

        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heapq.heappop(heap)
        
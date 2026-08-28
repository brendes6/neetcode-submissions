class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        """
        Strategy: djikstra's. Use a min heap to track which
        nodes have the shortest distance from source, and pop closest
        node off, while tracking time and which nodes we have seen.

        At end of search, return whether we have seen all nodes
        """
        import heapq

        seen = set()


        heap = []

        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((v, t))
        
        heapq.heappush(heap, (0, k))

        min_time = -1
        while heap:
            time, node = heapq.heappop(heap)
            if node in seen:
                continue

            seen.add(node)
            min_time = time

            for v1, t1 in graph[node]:
                if v1 not in seen:
                    heapq.heappush(heap, (t1 + time, v1))
        
        return min_time if len(seen) == n else -1
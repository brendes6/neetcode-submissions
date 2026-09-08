class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        APproach: this problem is going to involve a queue and a bit of hashing
        to understand the most recent tiem we ran  a task. Approach:

        At any specific time, what we want to do is pick the next task based on
        which one was least recently ran. WE will enforce this by maintaining a queue
        that will store a (task, num_left, last_ran), and we will pop of the
        front of the queue, running a task, and adding it to the end having
        'ran' it at a specific time. Once we get this going, all values in the queue
        will be sorted by increasing order of time last ran, thus the one on the front
        was ran least recently. any time we run a task, we decrement the num left, possibly being done
        with it, and update the time it was last ran. Any time we reach a task where we ran it lesss than
        n cycles before current cycle, we have to increment time. return time once q is empty.

        """

        from collections import deque, Counter
        import heapq

        ct = Counter(tasks)
        heap = []

        num_items = 0
        for k, v in ct.items():
            heapq.heappush(heap, -v)
            num_items += 1
        
        dq = deque([])

        num_processed = 0
        time = 0

        while num_processed < num_items:
            # print(heap)
            # print(dq)
            # print(time)
            while dq and dq[0][0] <= time:
                heapq.heappush(heap, dq[0][1])
                dq.popleft()
            
            if not heap:
                time += 1
                continue
            
            left = heapq.heappop(heap)

            if left == -1:
                num_processed += 1
            elif n==0:
                heapq.heappush(heap, left+1)
            else:
                dq.append((time + n + 1, left+1))
            
            time += 1
        
        return time

        



        
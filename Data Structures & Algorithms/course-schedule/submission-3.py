class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        """
        Course schedule: approach is that we done some sort of graph traversal
        using relationships we get from the prereqs array. It tells us courses
        we can ONLY take after taking a certain course. Thus, we iterate the prereqs array
        building a graph of neighbors, and we also track which courses have no pre-reqs. We
        then run a graph search starting with all courses with pre-reqs, and recurse on
        the courses they unlock. Once all nodes have been visited, return whether we saw all

        Postmortem: did a good job solving this. So it is clearly a graph problem,
        but it breaks down into a bit of a specific level of rules of which nodes can be visited.
        The pre-reqs define not only a neighbor-like relationship of classes that taking one may unlock,
        but also a set of courses that must be taken before taking a specific course. Thus we have this approach:

        - We maintain a stack of all currently take-able classes 
        - For each class that this one is a pre-req for, there are multiple poss:
            - if this class only has this as a pre-req, its takeable
            - if it has more pre-reqs, we need to wait for those
        - Thus, we maintain a dict mapping nodes to ones it may unlock,
        and another one tracking how many pre-reqs a course has. Rather than
        tracking a set of pre-reqs, we simply track the NUMBER of pre-reqs, since
        the neighbor relationship already gives us info about nodes that can reach a class,
        thus if a class has 2, 3, and 4 as pre-reqs, only those 3 will reach it, and we can just
        decrement number of pre-reqs per. Thus, when we reach a class,
        we mark it as taken, and look at each one its a pre-req for. if its only pre-req left,
        add that class, otherwise decrement pre-reqs and wait for another class to complete thats a pre-req.

        """
        from collections import defaultdict

        graph = defaultdict(list)
        preq_g = defaultdict(int)

        c_set = set([i for i in range(numCourses)])

        for cls, pre in prerequisites:
            graph[pre].append(cls)
            preq_g[cls] += 1
            if cls in c_set:
                c_set.remove(cls)
        
        stack = list(c_set)

        while stack:
            c = stack.pop()

            for nbr_cls in graph[c]:
                if nbr_cls in c_set:
                    continue
                if preq_g[nbr_cls] > 1:
                    preq_g[nbr_cls] -= 1
                    continue
                
                c_set.add(nbr_cls)
                stack.append(nbr_cls)

        return len(c_set)==numCourses


        
        
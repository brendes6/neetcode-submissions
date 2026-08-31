class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        """
        Course schedule: approach is that we done some sort of graph traversal
        using relationships we get from the prereqs array. It tells us courses
        we can ONLY take after taking a certain course. Thus, we iterate the prereqs array
        building a graph of neighbors, and we also track which courses have no pre-reqs. We
        then run a graph search starting with all courses with pre-reqs, and recurse on
        the courses they unlock. Once all nodes have been visited, return whether we saw all

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


        
        
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        """Strategy: greedy type approach. we know that for
        any person whose weight == limit, we can immediately put that
        person on a boat. For anyone who is under weight limit, we need
        to match up the highest under-limit val to the lowest under-limit
        val available using two pointer approach. For example:

        [1, 2, 2, 3, 5, 6], limit=6

        In this situation, there is not disadvantage to pairing the 1 and the 4 since
        we can only pair TWO people - thus, the internal fragmenetation is not an issue
        or a bottleneck preventing less boats from being used.

        """

        people.sort()

        num_boats = 0

        l, r = 0, len(people) - 1

        # First handle that people == limit need own boat
        while r >= 0 and people[r] == limit:
            num_boats += 1
            r -= 1

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1

            num_boats += 1
            r -= 1
        
        return num_boats




class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Car fleet strategy: The solution here is that we need
        to make an array of when each car will arrive. THis will be
        the math.ceil((target - position) / speed) for each val.

        Once we have that, we create a stack and iterate this new array.
        For any val in the array, if it is less than or eq the most recent one, we don't add it.
        if it is > the val, we add it. at end we return size of stack
        """
        # Make array of sorted pos, speed car tuples, sorted decreasing by pos
        import math

        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)

        arrivals = [((target-p) / s) for p, s in cars]

        # print(arrivals)

        stack = []

        for a in arrivals:
            if not stack or a > stack[-1]:
                stack.append(a)
        
        return len(stack)

        """
        Postmortem: struggled a tiny bit with this one but eventually figured out the issue.

        This is a tough one because it requires understanding both how you should structure the problem
        for max simplicity (sorted cars by position, calculating arrival times) and what ds to use.

        Ultimately, when you sort the cars by position, you can understand the order of cars and when they are expected
        to arrive. If a car is behind another car and will arrive earlier than it, it will catch up. If a car is behind
        another and will arrive later than it, it will never catch up. Thus, we can maintain a stack where we only ever
        add to the stack if we encounter a car that won't catch up to the bottlenecking one in front of it - we can disregard
        all other cars that will catch up to a specific one since they will just form a fleet.
        """
        
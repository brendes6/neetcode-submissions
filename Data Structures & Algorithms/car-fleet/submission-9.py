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
        
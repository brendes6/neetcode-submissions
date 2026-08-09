class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        daily temperatures: another stack-based problem. So the strategy here is to
        iterate the array and track each entries (temp, i) in a tuple and add that
        tuple to a stack. every time we add a entry to stack, we pop any values who have
        temp < this val's temp off an place their value into a ret array
        based on the diff between the two val's i's.
        """

        ret = [0] * len(temperatures)

        stack = []

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, i))
                continue
            
            while stack and stack[-1][0] < temp:
                _, j = stack.pop()
                ret[j] = i-j
            
            stack.append((temp, i))
        
        return ret
        
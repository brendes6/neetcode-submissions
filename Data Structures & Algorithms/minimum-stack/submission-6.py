class MinStack:
    """
    Min stack implementation: maintain two stacks, one containing vals,
    the second containing the min value BEFORE a certain one was added.
    Thus, we also track a current min val and:
    whenever we push, check if val is new min, if so update min val and push old one to msatck
    whenever we pop, pop the val from normal stack and set min val to popped from mstack
    getMin returns min
    """

    def __init__(self):
        self.stack = []
        self.mstack = []
        self.minVal = float('infinity')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mstack.append(self.minVal)

        self.minVal = min(self.minVal, val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minVal = self.mstack.pop()
        

    def top(self) -> int:
        if not self.stack:
            return -1
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minVal
        

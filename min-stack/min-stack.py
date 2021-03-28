class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            lastval, lastmin = self.stack[-1]
            self.stack.append((val, min(min(lastval, lastmin), val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        topval, topmin = self.stack[-1]
        return topval 

    def getMin(self) -> int:
        topval, topmin = self.stack[-1]
        return topmin


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
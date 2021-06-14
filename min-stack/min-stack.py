import heapq
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.pq = []
        self.min_ = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_ = min(self.min_, val)

    def pop(self) -> None:
        curr = self.stack.pop()
        if curr == self.min_: 
            self.min_ = float('inf')
            for num in self.stack:
                self.min_ = min(self.min_, num)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
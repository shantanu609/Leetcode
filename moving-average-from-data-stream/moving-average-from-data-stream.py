from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size 
        self.q = deque()
        self.total = 0 
        
    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            curr = self.q.popleft()
            self.total -= curr 
    
        self.q.append(val)
        self.total += val

        return self.total / len(self.q)
            


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
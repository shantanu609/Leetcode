class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dq = deque() 

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if not len(self.dq):
            self.dq.append([timestamp, 1])
        else:
            if self.dq[-1][0] != timestamp:
                self.dq.append([timestamp, 1])
            else:
                self.dq[-1][1] += 1 
        
        for i in range(len(self.dq)):
            if i < len(self.dq):
                a, b = self.dq[i]
                last = self.dq[-1][0]
                if last - a >= 300:
                    self.dq.popleft()
                else:
                    break 

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        lowerB, upperB = max(0, timestamp - 300), timestamp
        
        count = 0 
        for i in range(len(self.dq)):
            a, b = self.dq[i]
            if lowerB < a <= upperB:
                count += b 
        
        return count
        
"""
301 - 300 = 1
    301 -> lowerB = 2
           upperB = 301

"""
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

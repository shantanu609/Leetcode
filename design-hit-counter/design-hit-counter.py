from collections import OrderedDict
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = OrderedDict()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp not in self.d:
            self.d[timestamp] = 0 
        
        self.d[timestamp] += 1 
        
    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp <= 300:
            upperB = timestamp 
            return self.countHits(timestamp)
    
        else: 
            lowerB = timestamp - 300 
            list_ = []
            for k,v in self.d.items():
                if k > lowerB:
                    break 
                list_.append(k)
            for num in list_:
                self.d.pop(num)
            
            return self.countHits(timestamp)
        
    def countHits(self, upperB):
        count = 0 
        for k,v in self.d.items():
            if k > upperB:
                break 
            count += v 

        return count 


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

"""
    hits = [1,1,1,1,1,1,2,2,2,297, 3,4,5]
    
    target = 301
    lowerB = 1
    upperB = 301
    
    d = {
            1: 100,0000
            2: 250,000
            3: 14,000 
            4: 500 
            300: 
            301: 
    }
    
    target = 3 
    lower = max(1, 5-300) = 1 
    upper = 2
    
    result = j - i 
    
    l            r
    [1,1,1,1,1,1,2,5]    = r - l + 1 
    
    l                           m                         r
    [z,z,z,z,z,1,1,1,1, 1, 1,1,1,1,1,1,1,...(50), 2,2,2,2,2....2,2,(25), 3, 4, 5, 6, 7] = O(200)
"""
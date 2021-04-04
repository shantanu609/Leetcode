import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = [] 
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        top = heapq.heappop(self.maxHeap)
        
        # add it to the minHeap 
        heapq.heappush(self.minHeap, -top)
        
        # balance 
        if len(self.minHeap) > len(self.maxHeap):
            top = heapq.heappop(self.minHeap)
            
            # insert it into maxHeap 
            heapq.heappush(self.maxHeap, -top)
        

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        
        first = -self.maxHeap[0]
        second = self.minHeap[0]
        
        return (first + second) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
import heapq
class Pair:
    def __init__(self, count, word):
        self.count = count 
        self.word = word 
    
    def __lt__(self, item):
        if self.count < item.count:
            return self.count < item.count 
        elif self.count == item.count:
            return self.word > item.word
        
from collections import deque
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for i in range(len(words)):
            if words[i] not in d:
                d[words[i]] = 0 
            
            d[words[i]] += 1 
        print(d)
        pq = []
        result = deque()
        for word, count in d.items():
            heapq.heappush(pq, Pair(count, word))
            
            if len(pq) > k:
                heapq.heappop(pq)
        
        while pq:
            p = heapq.heappop(pq)
            result.appendleft(p.word)
        
        return result 
            
        
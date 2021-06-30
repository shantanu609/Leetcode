import heapq
class Pair:
    def __init__(self, word, count):
        self.word = word 
        self.count = count 
    
    def __lt__(self, other):
        if self.count == other.count: 
            return self.word > other.word 
        
        return self.count < other.count
        
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        pq = [] 
        d = {}
        res = [] 
        
        for word in words:
            if word not in d: 
                d[word] = 0 
            
            d[word] += 1 
        
        for word, count in d.items():
            heapq.heappush(pq, Pair(word, count))
        
            if len(pq) > k: 
                heapq.heappop(pq)
        
        while pq : 
            res.append(heapq.heappop(pq).word)
            
        
        return res[::-1]
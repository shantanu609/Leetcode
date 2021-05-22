import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = [] 
        for i in range(len(points)):
            dist = self._calcEuclDist(points[i])
            heapq.heappush(pq, (-dist, i, points[i]))
            
            if len(pq) > k:
                heapq.heappop(pq)
        
        result = [] 
        while pq:
            dist, indx, point = heapq.heappop(pq)
            result.append(point)
        
        return result
    
    def _calcEuclDist(self, point):
        x, y = point
        
        dist = ((x ** 2) + (y ** 2)) ** (1/2)
        
        return dist
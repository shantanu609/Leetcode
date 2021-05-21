import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            heapq.heappush(pq, num)
            
            if len(pq) > k:
                heapq.heappop(pq)
        
        result = heapq.heappop(pq)
        return result
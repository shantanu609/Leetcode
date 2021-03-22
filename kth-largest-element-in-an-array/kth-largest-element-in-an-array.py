import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
            nums = [3,2,1,5,6,4], k = 2
            
            heap = [5,6]
        """
        pq = [] 
        for i in range(len(nums)):
            heapq.heappush(pq, nums[i])
            if len(pq) > k:
                heapq.heappop(pq)
        
        result = heapq.heappop(pq)
    
        return result
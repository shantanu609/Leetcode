import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 0 
            d[nums[i]] += 1 
        
        pq = [] 
        for num, count in d.items():
            heapq.heappush(pq, (count, num))
            if len(pq) > k:
                heapq.heappop(pq)
        res = []
        while pq:
            curr = heapq.heappop(pq)
            res.append(curr[1])
        
        return res
        
        
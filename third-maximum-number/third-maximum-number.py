import heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        sol1:
            [3, 4, 2, 1, 5, 6, 5, 6, 7]   3rdmax = 4
                                        i
            set = {3, 4, 2, 1, 5, 6, 7}
            
            minHeap = [5, 6, 7]  => len() > 3 ? pop() : continue 
            
            return minHeap.pop() => 5
            
            # Time = O(nlog3) = O(n)
            # Space = O(n) + O(3)
            
        sol2 : Quick select 
            if len(nums) < 3: max(nums)
            else:
                quick_select -> len(nums)-3
        """
        
        # if len(nums) < 3:
        #     return max(nums)
        
        set_ = set()
        pq = []
        
        for i in range(len(nums)):
            if nums[i] not in set_:
                set_.add(nums[i])
                heapq.heappush(pq, nums[i])
            
                if len(pq) > 3:
                    heapq.heappop(pq)
        
        if len(pq) < 3:
            res = 0 
            while pq:
                res = heapq.heappop(pq)
            return res 
        
        return heapq.heappop(pq)
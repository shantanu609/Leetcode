from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0 
        minDq = deque()
        maxDq = deque()
        
        l, r = 0, 0 
        
        while r < len(nums):
            
            # start removing elements from the minDq if there is a smaller number than last elem in minDq 
            while minDq and nums[r] <= nums[minDq[-1]]:
                minDq.pop()
            
            # start removing elements from the maxDq if there is a larger element that the last elem in maxDq
            while maxDq and nums[r] > nums[maxDq[-1]]:
                maxDq.pop()
            
            # insert right pointer in both the dq 
            minDq.append(r)
            maxDq.append(r)
            
            # remove elements which violates the limit if the diff is greater than limit 
            while minDq and maxDq and abs(nums[minDq[0]] - nums[maxDq[0]]) > limit: 
                
                # increase the left pointer because of violation 
                l += 1 
                
                # remove index from minDq if left has moved ahead 
                if l > minDq[0]:
                    minDq.popleft()
                
                # remove the index from maxDq if left has moved ahead 
                if l > maxDq[0]:
                    maxDq.popleft()
        
            
            # get the length of the subarray which is statisifying the condition of limit 
            res = max(res, r - l + 1)
            
            # increase the right pointer 
            r += 1 
        return res
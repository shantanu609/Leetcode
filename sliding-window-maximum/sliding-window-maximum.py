from collections import deque 
class Solution:
    dq = None 
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # initialize the result and deque
        res = [] 
        self.dq = deque() 
        maxIndex = 0 
        
        # loop through first k elements 
        for i in range(k):
            # clean the deque 
            self.cleanDeque(i, nums, k)
            
            # append into the deque 
            self.dq.append(i)
            
            # check for the maximum element in the first k array elements
            if nums[maxIndex] < nums[i]:
                maxIndex = i 
        
        res.append(nums[maxIndex])
        
        # lopp through remaining k to n elements 
        for i in range(k, len(nums)):
            self.cleanDeque(i, nums, k)
            self.dq.append(i)
            res.append(nums[self.dq[0]])
        
        return res 
        
    def cleanDeque(self, i, nums, k):
        # check if window has exceeded? if yes then remove 0th index 
        if self.dq and self.dq[0] == i - k:
            self.dq.popleft()
        
        # pop all smaller elements, smaller than nums[i]
        while self.dq and nums[i] > nums[self.dq[-1]]:
            self.dq.pop()
            
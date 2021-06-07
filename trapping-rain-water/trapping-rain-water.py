class Solution:
    def trap(self, height: List[int]) -> int:
        l1 = l2 = 0 
        res = 0 
        
        left, right = 0, len(height) - 1 
        
        while left <= right: 
            if l1 <= l2: 
                
                if l1 >= height[left] :
                    res += l1 - height[left]
                else: 
                    l1 = height[left]
                    
                left += 1
                
            else:
                
                if l2 >= height[right]: 
                    res += l2 - height[right]
                
                else:
                    l2 = height[right]
                    
                right -= 1 
        
        
        return res
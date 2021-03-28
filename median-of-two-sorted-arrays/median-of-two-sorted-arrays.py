class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
    
        left, right = 0, n1 
        """
                x1. x2
                2 | 3 
                4 | 5
                y1. y2
        """
        while left <= right:
            
            xPart = (right + left) // 2 
            yPart = (n1 + n2 + 1) // 2 - xPart 
            
            # check for each partition x1 x2 y1 y2 values 
            x1, x2, y1, y2 = 0, 0, 0, 0
            
            if xPart == 0:
                x1 = float('-inf')
            else:
                x1 = nums1[xPart - 1]
            
            if xPart == n1:
                x2 = float('inf')
            else:
                x2 = nums1[xPart]
            
            if yPart == 0:
                y1 = float('-inf')
            else:
                y1 = nums2[yPart - 1]
            
            if yPart == n2:
                y2 = float('inf')
            else:
                y2 = nums2[yPart]
            
            
            print(x1,x2,y1,y2)
            
            # check if both the partitions are valid 
            if x1 <= y2 and y1 <= x2: 
                # found median 
                # if even
                if (n1 + n2) % 2 == 0:
                    a = max(x1, y1)
                    b = min(x2, y2)
                    return (a+b) / 2 
                
                # if odd
                else:
                    return max(x1, y1)
            
            elif x1 > y2 :
                right = xPart - 1 
            
            else:
                left = xPart + 1 
        
        raise "Value Error"
                
            
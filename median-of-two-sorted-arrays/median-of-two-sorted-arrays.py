class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """       
                1 2 3  4 |      num1 x
                
                | 5 6  7  8       num2 y
                 
                xmax = 1  xmin = 2
                ymax = 7  ymin = 8
                    
                if xmax <= ymin and ymax <= xmin:
        """
       
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        left, right = 0, len(nums1)
        while left <= right:
            xPart = (left + right) // 2 
            yPart = (n1 + n2 + 1) // 2 - xPart 

            xmax, xmin, ymax, ymin = 0, 0, 0, 0

            if xPart == 0:
                xmax = float('-inf')
            else:
                xmax = nums1[xPart - 1]

            if xPart == len(nums1):
                xmin = float('inf')
            else:
                xmin = nums1[xPart]

            if yPart == 0:
                ymax = float('-inf')
            else:
                ymax = nums2[yPart - 1]

            if yPart == len(nums2):
                ymin = float('inf')
            else:
                ymin = nums2[yPart]
        
            if xmax <= ymin and ymax <= xmin:
                # check for even condition 
                if (n1 + n2) % 2 == 0:
                    x = max(xmax, ymax)
                    y = min(xmin, ymin)
                    return (x + y) / 2
            
                else:
                    # odd 
                    return max(xmax, ymax)
        
            elif xmax > ymin:
                right = xPart - 1 
            else:
                left = xPart + 1 
        
        
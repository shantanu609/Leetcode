class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0 
        last = 1
        for i in range(1, x):
            if i*i <= x:
                last = i 
            else:
                break 
        
        return last
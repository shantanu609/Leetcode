class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0 
        
        if num % 9 == 0: 
            return 9 
    
        return num % 9 
    
"""
10 = 9 + 1 
100 = 99 + 1 
1000 = 999 + 1 
"""
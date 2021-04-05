class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        odd = 1 
        even = x 
        flag = True if n < 0 else False 
        n = abs(n)
        
        while n > 0:
            if n % 2 == 1:
                odd = odd * even 
            
            even = even * even 
            n = n//2
        if flag: 
            return 1/odd 
    
        return odd
class Solution:
    def reverse(self, x: int) -> int:
        """
            nums = 123   size = 3
                  
                    res = 3 
                    1) 3 : res = res * 10 + mod = 0 x 10 + 3 = 3 
                    2) 2 : res = res * 10 + mod = 3 x 10 + 2 = 32 
                    3) 1 : res = res * 10 + mod = 32 x 10 + 1 = 321 
            
            nums = 12,000
        """
        if x == 0:
            return 0 
        
        res = 0 
        flag = False 
        if x < 0:
            flag = True 
            x = x * -1 
        
        res = 0 
        while x > 0:
            # take mod 
            lastDigit = x % 10 
            res = res * 10 + lastDigit 
            x = x // 10 
        
        if res < (-2**31) or res > (2**31) - 1:
            return 0 
        
        if flag:
            return -1 * res 
        
        return res 
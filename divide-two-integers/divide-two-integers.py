class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return (2**31) - 1
        
        if dividend == 0:
            return 0
    
        if (dividend < - 2**31 or dividend > 2**31 -1) and (divisor == 1):
            return (2**31) - 1 
    
        if dividend == 1 and (divisor < -2**31 or divisor > 2**31 - 1):
            return 0 
    
        quotient = 0
        newDivisor = abs(divisor)
        newDividend = abs(dividend)
        
        while newDividend >= newDivisor:
            shift = 0 
            
            while (newDivisor << shift) <= newDividend:
                shift += 1 
            
            shift -= 1 
        
            quotient += (1 << shift)
            
            newDividend -= newDivisor << shift 
        
        if dividend < 0 and divisor < 0: 
            return self._getResult(quotient)
    
        if dividend > 0 and divisor > 0:
            return self._getResult(quotient)
        
        return -quotient 
    
    def _getResult(self, quotient):
        if quotient > (2**31 -1 ):
            quotient =  (2**31 - 1)
        
        elif quotient < (-2**31):
            quotient = (2**31 - 1)
        
        return quotient 
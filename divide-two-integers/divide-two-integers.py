class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # edge case 
        if dividend <= (-2**31) and divisor == -1:
            return (2**31)-1
        
        ldividend, ldivisor = abs(dividend), abs(divisor)
        result = 0 
        
        while ldividend >= ldivisor:
            shift = 0 
            
            while (ldivisor << shift)  <= ldividend:
                shift += 1 
            
            shift -= 1 
            
            result = result + (1 << shift)
            
            ldividend = ldividend - (ldivisor << shift)
        
        if dividend < 0 and divisor < 0:
            return result 
        
        if dividend > 0 and divisor > 0:
            return result 
        
        return -result 
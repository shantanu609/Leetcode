class Solution:
    def calculate(self, s: str) -> int:
        result = 0 
        sign = 1    # 1 for positive and -1 for negative 
        stack = [] 
        num = 0 
        
        for ch in s:
            if ch == ' ':
                continue 
            
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            elif ch == '+':
                result = result + (num * sign)
                sign = 1    # since we are in '+'
                num = 0 
            
            elif ch == '-':
                result = result + (num * sign)
                sign = -1 
                num = 0 
            
            elif ch == '(':
                stack.append(result)
                stack.append(sign)
                sign = 1 
                result = 0 
                operand = 0 
            
            elif ch == ")":
                result = result + (sign * num)
                
                result = result * stack.pop()   # multiply the sign 
                
                result = result + stack.pop()   # add the previous result 
                
                num = 0 
            
            
        return result + (sign * num)
                
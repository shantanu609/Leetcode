class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        for i in range(len(s)):
            char = s[i]
            
            if char == '(' or char == '[' or char == '{' :
                stack.append(char)
                continue 
            
            if not stack:
                return False 
            
            last = stack.pop()
            
            if char == ')' and last != '(':
                return False 
            
            if char == ']' and last != '[':
                return False 
            
            if char == '}' and last != '{':
                return False 
        
        if stack:
            return False 
        
        return True
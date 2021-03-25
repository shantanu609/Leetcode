class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        for i in range(len(s)):
            ch = s[i]
            
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            
            else:
                if not stack:
                    return False 
                
                if ch == '}' and stack[-1] != '{':
                    return False 
                
                if ch == ')' and stack[-1] != '(':
                    return False 
                
                if ch == ']' and stack[-1] != '[':
                    return False 
                
                stack.pop()
            
        if len(stack) > 0:
            return False 
        
        return True 
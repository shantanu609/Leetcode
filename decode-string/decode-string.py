class Solution:
    def decodeString(self, s: str) -> str:
        """
                "3 [ a 2 [ c ] ]"
                 i
        """
        if len(s) == 0:
            return ''
        
        stack = [["", 1]]
        num = 0 
        
        for i in range(len(s)):
            ch = s[i]
            
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            elif ch == '[':
                stack.append(["", num])
                num = 0 
            
            elif ch.isalpha():
                stack[-1][0] += ch 
            
            elif ch == ']':
                curr = stack.pop()
                stack[-1][0] += curr[0] * curr[1]
    
        return stack[0][0]
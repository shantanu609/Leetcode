class Solution:
    def decodeString(self, s: str) -> str:
        stack = [["", 1]]
        num = 0 
        
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            
            elif s[i] == '[':
                stack.append(["", num])
                num = 0 
            
            elif s[i].isalpha():
                stack[-1][0] += s[i]
            
            elif s[i] ==']':
                string, count = stack.pop()
                stack[-1][0] += string * count
        
        return stack[0][0]
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            '{' : '}',
            '(' : ')',
            '[' : ']'
         }
        
        for i in range(len(s)):
            ch = s[i] 
            if ch in d:
                stack.append(d[ch])
            else:
                if stack and ch == stack[-1]:
                    stack.pop()
                else:
                    return False 
        
        return len(stack) == 0
from collections import deque
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        q = deque()
        right = len(s) - 1
        count = 0 
        
        while right >= 0:
            if s[right] == '-':
                right -= 1 
                continue 
            
            if not s[right].isalpha(): 
                q.appendleft(s[right])
            else:
                q.appendleft(s[right].upper())
            count += 1 
            
            if count == k: 
                count = 0 
                q.appendleft('-')
            
            right -= 1 
        
        if q and q[0] == '-':
            q.popleft() 
            
        return ''.join(q)
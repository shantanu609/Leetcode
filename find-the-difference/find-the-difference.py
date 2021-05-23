class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {} 
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 0 
            
            d[s[i]] -= 1 
        
        
        for i in range(len(t)):
            if t[i] in d:
                d[t[i]] += 1 
                
                if d[t[i]] > 0:
                    return t[i]
            
            else:
                return t[i]
            
        return ''
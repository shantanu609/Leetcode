class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {} 
        for i in range(len(s)):
            if s[i] not in d: 
                d[s[i]] = 0 
            d[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in d:
                return False 
            d[t[i]] -= 1 
            if d[t[i]] < 0:
                return False 
        
        for k,v in d.items():
            if v > 0:
                return False 
        
        return True 
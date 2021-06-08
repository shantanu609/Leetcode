class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # s = "cbaebabacd", p = "abc"
        
        if len(p) > len(s):
            return []
        
        mapP = {}
        for i in range(len(p)):
            if p[i] not in mapP:
                mapP[p[i]] = 0 
            
            mapP[p[i]] += 1 
        
        mapS = {} 
        result = [] 
        
        for i in range(len(s)):
            if s[i] not in mapS:
                mapS[s[i]] = 0 
                
            mapS[s[i]] += 1 
            
            if i >= len(p):
                if mapS[s[i-len(p)]] == 1: 
                    mapS.pop(s[i - len(p)])
                
                else:
                    mapS[s[i-len(p)]] -= 1 
            
            
            if mapP == mapS:
                result.append(i - len(p) + 1)
        
            
        return result
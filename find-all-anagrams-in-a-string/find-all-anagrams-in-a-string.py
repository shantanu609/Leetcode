class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pmap = {} 
        for i in range(len(p)):
            if p[i] not in pmap:
                pmap[p[i]] = 0 
            
            pmap[p[i]] += 1 
        
        smap = {} 
        result = [] 
        
        for i in range(len(s)):
            if s[i] not in smap:
                smap[s[i]] = 0 
            
            smap[s[i]] += 1 
            
            if i >= len(p):
                if smap[s[i - len(p)]] == 1:
                    smap.pop(s[i - len(p)])
                    
                else:
                    smap[s[i - len(p)]] -= 1 
            
            if smap == pmap:
                result.append(i + 1 - len(p))
        
        return result
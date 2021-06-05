from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = OrderedDict()
        
        for i in range(len(s)):
            if s[i] not in d: 
                d[s[i]] = [i,0]
            
            d[s[i]][1] += 1 
        
        for k, v in d.items():
            index, count = v
            if count == 1 :
                return index 
        
        return -1
            
         
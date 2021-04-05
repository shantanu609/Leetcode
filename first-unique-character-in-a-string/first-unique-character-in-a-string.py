from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = OrderedDict()
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = [0,i]
            
            d[s[i]][0] += 1 
    
        
        for key, value in d.items():
            if value[0] == 1 :
                return value[1] 
        
        return -1
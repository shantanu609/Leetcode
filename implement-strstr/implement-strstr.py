class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0 
        if len(haystack) == 0 or len(haystack) < len(needle):
            return -1 
        """
           haystack= [h e l l o z z z z h l l e]  
                 i
            
            neddle = lle
            
            
            mapHayStack = {
            
                    l: [2, 3, 10, 11]
            } 
                            [3 : 3 + len(neddle) + 1]
        """
        d = {}
        for i in range(len(haystack)):
            ch = haystack[i]
            if ch not in d:
                d[ch] = [] 
            
            d[ch].append(i)
        
        if needle[0] not in d :
            return -1 
        targetList = d[needle[0]]
        
        for indx in targetList:
            if haystack[indx : indx + len(needle)] == needle:
                return indx
        
        return -1
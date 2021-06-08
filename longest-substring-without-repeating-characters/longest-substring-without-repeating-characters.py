class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {} 
        i = 0 
        j = 0 
        res = 0 
        while j < len(s):
            if s[j] not in d:
                d[s[j]] = j 
                j += 1 
                continue 
            
            res = max(res, j-i)     
            i = max(i, d[s[j]] + 1)
            
            d[s[j]] = j 
            j += 1 
        res = max(res, j-i)     
        return res
            
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        i, j = 0, 0 
        res = 0 
        
        while i < len(s):
            while j < len(s):
                if s[j] not in d:
                    d[s[j]] = j 
                    j += 1
                    res = max(res, j - i)
                else:
                    if i <= d[s[j]]:
                        i = d[s[j]] + 1 
                    d[s[j]] = j
                    j += 1 
                    res = max(res, j - i)
            i += 1
        
        return res
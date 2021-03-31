class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        d = {}
        a = 65
        for i in range(65, 65+26):
            d[chr(i)] = i - a + 1 
        
        res = 0 
        for ch in columnTitle:
            res = res * 26 + d[ch]
        
        return res
            
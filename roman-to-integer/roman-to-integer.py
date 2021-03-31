class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I' : 1, 
            'IV': 4,
            'V' : 5,
            'IX': 9,
            'X' : 10, 
            'XL': 40,
            'L' : 50,
            'XC': 90,
            'C' : 100,
            'CD': 400,
            'D' : 500,
            'CM': 900,
            'M' : 1000,
        }
        
        res = 0 
        i = 0 
        while i < len(s):
            temp = d[s[i]] if s[i] in d else 0 
            if i+1 < len(s) and s[i: i+2] in d :
                temp = d[s[i:i+2]]
                i += 2 
                res += temp 
            else:
                res += temp
                i += 1 
        
        return res
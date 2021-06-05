class Solution:
    def modifyString(self, s: str) -> str:
        d = {}
        s = list(s)

        for i in range(len(s)):
            if s[i] != '?':
                d[s[i]] = i 
                continue 
                
            for j in range(1, 26+1):
                char = chr(96 + j)
                if (i > 0 and s[i-1] == char) or (i < len(s) - 1 and s[i+1] == char):
                    continue 
                # if (i > 0 and s[i-1] != char) or (i < len(s) - 1 and s[i+1] != char):
                s[i] = char 
                d[char] = i 
                break 
                # else:
                #     s[i] = char
                    
        return ''.join(s)
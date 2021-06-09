class Solution:
    def lengthLongestPath(self, input: str) -> int:
        res = 0 
        d = {0 : 0} 
        
        for line in input.splitlines():
            path = line.lstrip('\t')

            depth = len(line) - len(path)
            
            if '.' in path: 
                res = max(res, d[depth] + len(path))
        
            else: 
                d[depth + 1] = d[depth] + len(path)  + 1 
        
        return res
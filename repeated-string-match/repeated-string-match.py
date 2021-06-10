class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        sb = []
        count = 0
        
        while len(sb) < len(b):
            count += 1 
            for char in a:
                sb.append(char)
            
        if b in ''.join(sb):
            return count 
    
        for char in a:
            sb.append(char)
        
        if b in ''.join(sb):
            return count + 1 
    
        return -1
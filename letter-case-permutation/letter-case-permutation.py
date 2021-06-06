class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.res = set() 
        self.backtrack(list(s), 0, [])
        return list(self.res)
    
    def backtrack(self, s, indx, path):
        # base case 
        if indx == len(s):
            if len(path) == len(s):
                self.res.add(''.join(path))
            return 
        
        # logic 
        for i in range(indx, len(s)):
            char = s[i]
            
            path.append(char)
            
            self.backtrack(s, i+1, path)
            
            last = path.pop() 
            
            if last.isalpha() and last.islower():
                s[i] = last.upper()
                
                path.append(s[i])
                self.backtrack(s, i+1, path)
                path.pop() 
                
                s[i].lower()
            
            elif last.isalpha() and last.isupper():
                s[i] = last.lower() 
                
                path.append(s[i])
                self.backtrack(s, i+1, path)
                path.pop() 
                
                s[i].upper()
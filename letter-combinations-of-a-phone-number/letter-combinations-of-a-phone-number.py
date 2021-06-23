class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # edge case 
        if len(digits) == 0:
            return ''
        self.res = [] 
        self.d = {
            '2' : "abc",
            "3" : "def",
            "4" : "ghi", 
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv", 
            "9" : "wxyz"
        }
        
        self.backtrack(digits, 0, [])
        return self.res 
    
    def backtrack(self, digits, indx, path):
        # base case 
        if indx == len(digits):
            self.res.append(''.join(path))
            return 
        
        # logic 
        letters = self.d[digits[indx]]
        
        for i in range(len(letters)):
            # action 
            path.append(letters[i])
            
            # recurse 
            self.backtrack(digits, indx+1, path)
            
            # backtrack
            path.pop()
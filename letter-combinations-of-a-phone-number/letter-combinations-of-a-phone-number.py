class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        d = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        } 
        
        self.res = [] 
        self.backtrack(digits, 0, [], d)
        return self.res 
    
    def backtrack(self, digit, indx, path, d):
        # base case 
        if indx == len(digit): 
            self.res.append(''.join(path))
            return
        
        # Logic 
        letters = d[digit[indx]]
        
        for i in range(len(letters)):
            # action 
            path.append(letters[i])
            
            # recurse 
            self.backtrack(digit, indx + 1, path, d)
            
            # backtrack
            path.pop()
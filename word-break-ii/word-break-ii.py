class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.res = [] 
        d = set(wordDict)
        
        self.backtrack(s, 0, d, [])
        return self.res
    
    def backtrack(self, string, indx, d, path):
        # base case 
        if indx == len(string):
            self.res.append(' '.join(path))
            return 
        
        # logic 
        for i in range(indx, len(string)):
            # action
            word = string[indx : i + 1]
            
            # recurse 
            if word in d: 
                path.append(word)
                self.backtrack(string, i+1, d, path)
            
            # backtrack
            if path and path[-1] == word:
                path.pop()
class Solution:
    res = None 
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.res = []
        wordDict = set(wordDict)
        self.backtrack(s, 0, wordDict, [])
        # print(self.res)
        return self.res 
    
    def backtrack(self, s, indx, wordDict, temp):
        # base case 
        if indx == len(s):
            self.res.append(''.join(temp).rstrip())
            return True 
        
        # logic 
        for i in range(indx, len(s)):
            substring = s[indx : i+1]
            if substring in wordDict:
                temp.append(substring)
                temp.append(' ')
                self.backtrack(s, i+1, wordDict, temp)
                    # res = ''.join(temp)
                    # # self.res.append(res)
                    # return True 
                temp.pop()
                temp.pop()
        
        return False 
class Solution:
    output = None 
    
    def numDecodings(self, s: str) -> int:
        
        return self.recurse(s, 0)
        
    @lru_cache(maxsize = None)
    def recurse(self, s , indx):
        # base case 
        if indx == len(s):
            return 1

        if s[indx] == '0':
            return 0
        
        if indx == len(s) - 1:
            return 1 

        # logic 
        # get the substring single digit 
        answer = self.recurse(s, indx + 1)
        # get the substring two digit
        if int(s[indx: indx + 2]) <= 26:
            answer += self.recurse(s, indx + 2)
        
        return answer
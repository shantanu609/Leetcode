class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = float('-inf')
        self.string = ''
        for i in range(len(s)):
            self.helper(s, i, i)
            self.helper(s, i, i+1)
        
        return self.string 
    
    def helper(self, string, left, right): 
        
        while left >= 0 and right < len(string):
            if string[left] == string[right]:
                if self.res <= right - left + 1: 
                    self.res = right - left + 1 
                    self.string = string[left : right + 1]
                left -= 1 
                right += 1 
            else:
                break 
            
        
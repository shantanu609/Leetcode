class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        
        while i < j: 
            if s[i] != s[j]:
                #                           skip j                              skip i
                return self.checkPallindrome(s[i:j]) or self.checkPallindrome(s[i+1:j+1])
            i += 1 
            j -= 1 
        
        return True 
    
    def checkPallindrome(self, s):
        return s == s[::-1]
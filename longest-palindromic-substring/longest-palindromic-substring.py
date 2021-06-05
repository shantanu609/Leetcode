class Solution:
    
    endIndex, startIndex = None, None 
    def longestPalindrome(self, s: str) -> str:
        
        # Initialize the global variables 
        self.endIndex = 0 
        self.startIndex = 0 
        
        # Loop through the entire string 
        for indx in range(len(s)):
            
            # check for odd length Pallindrome 
            self.checkPallindrome(s, indx, indx)
            
            # check for even length Pallindrome 
            if indx + 1 < len(s): 
                self.checkPallindrome(s, indx, indx + 1)
        
        # return the result 
        return s[self.startIndex : self.endIndex + 1]
    
    def checkPallindrome(self, string, left, right):
        
        while left >= 0 and right < len(string) and string[left] == string[right]: 
            
            # update the global pointers
            if left >= 0 and right < len(string) and ((right - left) > (self.endIndex - self.startIndex)):
                self.endIndex = right 
                self.startIndex = left 
            
            left -= 1 
            right += 1 
    
class Solution:
    startIndex, endIndex = None, None 
    def longestPalindrome(self, s: str) -> str:
        
        # Initialize the global indexes 
        self.startIndex = 0 
        self.endIndex = 0 
        
        # Loop through the entire string s 
        for i in range(len(s)):
            
            # check for odd length pallindrome 
            self.isPalindromeHelper(s, i, i)
            
            # check for even legth pallindrome 
            if i+1 < len(s) and s[i] == s[i+1]:
                self.isPalindromeHelper(s, i, i+1)
        
        return s[self.startIndex : self.endIndex + 1]
    
    def isPalindromeHelper(self, s, left, right):
        while left <= right:
            
            # check if two pointers are within bound and character matches 
            if left >= 0 and right < len(s) and s[left] == s[right]: 
                
                # check if we have a longer substring then previous 
                if left >= 0 and right < len(s) and (self.endIndex - self.startIndex) < (right - left): 
                    
                    # if yes, then store the result
                    self.endIndex = right 
                    self.startIndex = left 
                
                # move the left pointer backwards and right pointer forward 
                left -= 1 
                right += 1 
            
            else:
                # if the character is not matching then dont loop further 
                break 
        
        
            
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        for i in range(len(s)):
            ch = s[i]
            if ch.isdigit():
                string.append(ch)
            elif ch.isalpha():
                string.append(ch.lower())
            else:
                continue 
            
        return self.checkPalindrome(string)
    
    def checkPalindrome(self, string):
        low = 0 
        high = len(string) - 1
        
        while low < high:
            if string[low] != string[high]:
                return False 
            
            low += 1 
            high -= 1 
        
        return True 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha = [0] * 26
        for i in range(len(s)):
            indx = ord(s[i]) - ord('a')
            alpha[indx] += 1 
        
        for i in range(len(t)):
            indx = ord(t[i]) - ord('a')
            
            alpha[indx] -= 1 
            
            if alpha[indx] < 0:
                return False
        
        for num in alpha:
            if num > 0:
                return False 
        
        return True
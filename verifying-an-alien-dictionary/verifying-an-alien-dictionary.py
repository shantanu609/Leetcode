class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {} 
        for i in range(len(order)):
            d[order[i]] = i 
       
        for i in range(len(words)-1):
            if self.helper(words[i], words[i+1], d) == False:
                return False 
        
        return True 
    
    def helper(self, word1, word2, d): 
        for i in range(len(word1)): 
            if i >= len(word2) or d[word1[i]] > d[word2[i]]:
                return False 
            
            if word2[i] == word1[i]:
                continue 
            
            if d[word1[i]] < d[word2[i]]:
                break
        
        return True 
            
    
"""
order = "worldabcefghijkmnpqstuvxyz"
words = ["word","world","row"]

   i
world
wor 
"""
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        set_ = set(words)

        res = [] 
        for word in words:
            if self.dfs(word, set_):
                res.append(word)
    
        return res
    
    def dfs(self, word, set_):
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            
            if prefix in set_ and suffix in set_:
                return True 
            
            if prefix in set_ and self.dfs(suffix, set_): 
                return True 
            
            if suffix in set_ and self.dfs(prefix, set_):
                return True 
        
        return False
class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        """
            d = {    String : Set()
            
                    'great' : [good, fine, ok]
                    
                    'good' : [great, fine, ok]
                    
                    'fine' : [good, ok, great]
            }
            
            great = good = fine = ok = great    
            
            
            great = good 
            good = fine 
            thereofre, great == fine
            
            "Hi, this, is, Sun"
            "Hi, this in,  Sun"
            
            {
                'Hi' : [hi]
            }
            
            
            word1   ?   word2
        """
        if len(words1) != len(words2):
            return False 
        
        d = {}
        
        for pair in pairs:
            first, second = pair 
            
            if first not in d: 
                d[first] = set()
            
            d[first].add(second)
            
            if second not in d :
                d[second] = set()
            
            d[second].add(first)
            
            # temp = d[first]
            
#             for word in d[second]:
#                 temp.add(word)
            
#             d[first] = temp
#             d[second] = temp
        
        
        for i in range(len(words1)):
            if words1[i] == words2[i]:
                continue 
                
            if words1[i] not in d or words2[i] not in d:
                return False 
            
            visited = set()
            
            if self.dfs(d, d[words1[i]], words2[i], visited) == False:
                return False 
        
        return True 
    
    
    def dfs(self, d, set_, target, visited):
        
        # print(array)
        if target in set_:
            return True 
        
        for word in set_:
            if word not in visited:
                visited.add(word)
                
                newSet = d[word]
                
                if self.dfs(d, newSet, target, visited):
                    return True 
                
        
        return False 
            
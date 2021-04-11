class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        """
                sentence1 = ["great","acting","skills", "fine", "fine", "great"]
                sentence2 = ["fine","drama","talent",   "great",   "good"]
                
                d = {
                        "great" : [fine]
                        "acting" : ["drama"]
                        "skills" : ["talent"]
                        "fine" : ["good"]
                }
                    
                    
                great = good 
                good = awesome          great != awesome
                
                great : [good]
                good : [great, awesome]
                awesome: [good]
        """
        # base cases
        if len(sentence1) != len(sentence2):
            return False 
        
        
        d = {} 
        
        for pair in similarPairs:
            first, second = pair 
            if first not in d:
                d[first] = []
            
            d[first].append(second)
            
            if second not in d:
                d[second] = []
            
            d[second].append(first)
        
        for i in range(len(sentence1)):
            firstWord = sentence1[i]
            secondWord = sentence2[i]
            
            if firstWord == secondWord:
                continue 
                
            if firstWord not in d or secondWord not in d:
                if firstWord != secondWord:
                    return False 
    
            
            if secondWord not in d[firstWord]:
                return False 
    
        return True
        
        
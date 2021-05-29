class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        d = {}
        for i in range(len(wordsDict)):
            word = wordsDict[i]
            
            if word not in d:
                d[word] = [] 
            
            d[word].append(i)
        
        
        res = float('inf')
        
        for indx1 in d[word1]:
            for indx2 in d[word2]:
                res = min(res, abs(indx1 - indx2))
            
        return res

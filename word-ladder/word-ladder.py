from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = {}
        for word in wordList:
            d[word] = 1 
        
        if endWord not in d: 
            return 0 
        
        q = deque([beginWord])
        result = 0 
        
        while q: 
            size = len(q)
            result += 1 
            for _ in range(size):
                curr = q.popleft() 
                
                similarWords = self.helper(curr, d)
                
                for word in similarWords: 
                    if word  == endWord:
                        return result + 1 
                    
                    if word in d:
                        q.append(word)
                        d.pop(word)
        
        return 0
                
        
        return result 
    
    def helper(self, word, d):
        wordCollection = set()
        word = list(word)
        for i in range(len(word)):
            ch = word[i]
            
            for j in range(97, 97 + 26 + 1):
                word[i] = chr(j)
                newWord = ''.join(word)
                if newWord in d: 
                    wordCollection.add(''.join(word))
            
            word[i] = ch 
        
        return wordCollection
            
        
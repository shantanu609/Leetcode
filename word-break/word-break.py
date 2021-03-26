from collections import deque 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        visited = set()
        q = deque()
        q.append(0)
        
        while q:
            currIndx = q.popleft()
            if currIndx in visited:
                continue 
            
            for i in range(currIndx, len(s)):
                # get the substring 
                substring = s[currIndx : i + 1]
                if substring in wordDict:
                    q.append(i+1)
                    
                    if i+1 == len(s):
                        return True 
                visited.add(currIndx)    
        
        return False 
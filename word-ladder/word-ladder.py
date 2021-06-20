from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # edge cases 
        if beginWord == endWord:
            return 0 
        
        # initialize DS 
        visited = set() 
        q = deque([beginWord])
        wordList = set(wordList)
        result = 0 
        
        if endWord not in wordList:
            return 0 
        
        while q: 
            size = len(q)
            result += 1 
            for _ in range(size):
                
                curr = q.popleft()  
                visited.add(curr)
                
                if curr == endWord: 
                    return result 
                
                self.helper(curr, wordList, q, visited)
        
        return 0 
    
    
    def helper(self, word, wordList, q, visited):
        word = list(word)
        for i in range(len(word)):
            originalChar = word[i]
            for j in range(97, 97+26):
                
                char = chr(j)
                word[i] = char 
                
                newWord = ''.join(word)
                # print(newWord)
                if newWord in wordList and newWord not in visited: 
                    q.append(newWord)
            
            word[i] = originalChar

"""
    beginWord = "hit", 
    endWord = "cog", 
    wordList = ["hot","dot","dog","lot","log","cog", "hat"]
    
    count = 1 
                  i 
    begin word = "hit" -> "hot" ->
                       -> "hat"
    
Approach 1) Brute Froce = O(n ^ 26)
Approach 2) Trie -   
Approach 3) BFS 
"""
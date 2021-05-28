from collections import deque
class TrieNode: 
    def __init__(self):
        self.childrens = {}
        self.isEnd = False 
        self.word = ''
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def _insert(self, word):
        node = self.root 
        
        for char in word:
            if char not in node.childrens:
                node.childrens[char] = TrieNode()
            
            node = node.childrens[char]
        
        node.isEnd = True 
        node.word = word
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        root = trie.root 
        
        for word in words:
            trie._insert(word)
        
        return self._bfs(root)
    
        
    def _bfs(self, root):
        q = deque([root])
        result = ''
        
        while q:
            curr = q.popleft()
            
            for valueNode in curr.childrens.values():
                
                if valueNode.isEnd: 
                    q.append(valueNode)
                    
                    if len(result) < len(valueNode.word) or result > valueNode.word:
                        result = valueNode.word 
        
        
        return result
                        
"""
["t","ti","tig","tige","tiger"
,"e","en","eng","engl","engli","englis","english",
 "h","hi","his","hist","histo","histor","history"]

"""                
                
                

                
                
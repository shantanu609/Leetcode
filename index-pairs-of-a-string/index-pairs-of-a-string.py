class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.isEnd = False
    
class Trie: 
    def __init__(self):
        self.root = TrieNode()
    
    def _insert(self, word):
        node = self.root
        
        for ch in word:
            if ch not in node.childrens:
                node.childrens[ch] = TrieNode()
            
            node = node.childrens[ch]
        
        node.isEnd = True 
    
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie = Trie()
        
        for word in words:
            trie._insert(word)
        
        result = []
        i = 0
        root = trie.root
        
        for i in range(len(text)):
            if text[i] in root.childrens:
                end = i 
                node = root
                
                while end < len(text) and node and text[end] in node.childrens:
                    node = node.childrens[text[end]]
                    
                    if node.isEnd:
                        result.append([i, end])    
                    
                    end += 1
                
                
        return result
  
class TrieNode:
    def __init__(self):
        self.childrens = {} 
        self.isEnd = False 

class Trie:
    def __init__(self):
        self.root = TrieNode() 
    
    def insert(self, word):
        node = self.root
        for i in range(len(word)-1, -1, -1):
            char = word[i]
            if char not in node.childrens:
                node.childrens[char] = TrieNode() 
            
            node = node.childrens[char]
        
        node.isEnd = True 
    
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie() 
        for word in words: 
            self.trie.insert(word)
        
        self.ls = deque()

    def query(self, letter: str) -> bool:
        self.ls.appendleft(letter)
        node = self.trie.root 
        
        for i in range(len(self.ls)):
            char = self.ls[i]
            
            if node.isEnd:
                return True 
            
            if char not in node.childrens:
                return False
            
            node = node.childrens[char]
        
        return node.isEnd == True
        
       
        
# ["ab","ba","aaab","abab","baa"]


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
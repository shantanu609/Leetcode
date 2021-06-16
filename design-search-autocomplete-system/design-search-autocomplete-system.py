class TrieNode:
    def __init__(self):
        self.childrens = {} 
        self.isWord = False 
        self.w = None
        self.hot = 0 

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, rank):
        node = self.root
        
        for char in word: 
            if char not in node.childrens:
                node.childrens[char] = TrieNode()
            
            node = node.childrens[char]
        
        node.isWord = True 
        node.w = word 
        node.hot -= rank 
        
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.keyword = ''
        
        for i in range(len(times)):
            self.trie.insert(sentences[i], times[i])
        

    def input(self, c: str) -> List[str]:
        if c != '#':
            self.keyword += c 
            res = self.search(self.keyword)
            return [w for r, w in sorted(res)][:3]
        
        self.trie.insert(self.keyword, 1)
        self.keyword = ''
        return []
    
    def search(self, word):
        node = self.trie.root
        
        for char in word:
            if char not in node.childrens:
                return [] 
            
            node = node.childrens[char]
        
        return self.dfs(node)
    
    def dfs(self, node):
        res = []
        
        if node:
            if node.isWord: 
                res.append((node.hot, node.w))
            
            for k, v in node.childrens.items():
                res.extend(self.dfs(v))
        
        return res


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
from collections import defaultdict 
class Solution:
    prime = None 
    res = None 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        self.prime = [] 
        self.res = []
        self.getPrime(26)
        
        hashmap = defaultdict(list)
        
        for word in strs:
            hashVal = self.getHash(word)
            hashmap[hashVal].append(word)
        
        result = []
        for key, value in hashmap.items():
            result.append(value)
        
        return result 
    
    def getHash(self, word):
        res = 1 
        for ch in word:
            res = res * self.prime[ord(ch) - ord('a')]
        
        return res 
    
    def getPrime(self, n):
        num = 2 
        while len(self.prime) <= n:
            j = 2 
            
            while j < num and num % j != 0:
                j += 1
            
            if num == j:
                self.prime.append(num)
        
            num += 1
            
    
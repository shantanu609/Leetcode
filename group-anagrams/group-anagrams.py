class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        self.primes = []
        self.getPrimes()
        d = {}
        
        for word in strs:
            hashValue = self._hashFun(word)
            if hashValue not in d: 
                d[hashValue] = [] 
            
            d[hashValue].append(word)
        
        output = [] 
        for k, arr in d.items():
            output.append(arr)
        
        return output 
    
    
    def getPrimes(self):
        startNum = 2 
        
        while len(self.primes) <= 26: 
            
            divide = 2 
            
            while divide < startNum and startNum % divide != 0:
                divide += 1 
            
            if divide == startNum:
                self.primes.append(divide)
            
            startNum += 1
    
    
    def _hashFun(self, word):
        res = 1 
        for char in word: 
            index = ord(char) - ord('a')
            
            res = res * self.primes[index]
        
        return res
        
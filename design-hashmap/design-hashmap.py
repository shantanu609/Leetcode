class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 2000
        self.map = [None] * self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size 
        if self.map[index] == None:
            self.map[index] = [None] * self.size 
        
        self.map[index][key // self.size] = value 
   
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size 
        
        if self.map[index] == None:
            return -1 
    
        res = self.map[index][key//self.size] 
        
        if res is None:
            return -1 
        
        return res
 
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        
        index = key % self.size 
        if self.map[index] == None: 
            return 
        
        self.map[index][key // self.size] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
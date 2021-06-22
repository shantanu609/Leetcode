class ListNode:
    def __init__(self, k, v):
        self.k = k 
        self. v = v 
        self.next = None 
        
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 2069
        self.hashmap = [None for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        node = None 
        hash_key = self._getHash(key)
        if self.hashmap[hash_key] == None: 
            self.hashmap[hash_key] = ListNode(-1,-1)
            node = self.hashmap[hash_key]
        
        else: 
            tempNode = self.hashmap[hash_key]
            prev = None 
            
            while tempNode: 
                prev = tempNode 
                if tempNode.k == key:
                    tempNode.v = value
                    return 
                tempNode = tempNode.next 
            
            node = prev 
        
        node.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_key = self._getHash(key)
        tempNode = self.hashmap[hash_key]
        while tempNode:
            if tempNode.k == key: 
                return tempNode.v 
            tempNode = tempNode.next 
        
        return -1 

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_key = self._getHash(key)
        tempNode = self.hashmap[hash_key]
        
        if not tempNode: 
            return 
        
        prev = None 
        while tempNode: 
            if tempNode.k == key: 
                prev.next = tempNode.next 
                return 
            prev = tempNode 
            tempNode = tempNode.next 
        
    def _getHash(self, key):
        return key % self.size


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# 1,000,000
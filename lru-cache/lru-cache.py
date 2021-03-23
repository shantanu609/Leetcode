class Node:
    def __init__(self, key, val):
        self.key = key 
        self.val = val 
        self.prev = None 
        self.next = None 
        
class LRUCache:

    def __init__(self, capacity: int):
        self.storage = {}
        self.freq = {}
        self.count = 0 
        self.capacity = capacity 

    def get(self, key: int) -> int:
        if key not in self.storage:
            return -1 
        
        result = self.storage[key]
        self.freq[key] = self.count + 1 
        self.count += 1 
        # print(self.storage)
        # print(self.freq)
        # print(self.count)
        # print("---")
        return result

    def put(self, key: int, value: int) -> None:
        if key not in self.storage:
            if len(self.storage) == self.capacity:
                # need to evict LRU 
                tempkey, tempval = None, float('inf')
                for k, v in self.freq.items():
                    if v < tempval:
                        tempval = v 
                        tempkey = k 
                if tempkey:
                    self.storage.pop(tempkey)
                    self.freq.pop(tempkey)

                    
        self.storage[key] = value 
        self.freq[key] = self.count + 1 
        self.count += 1 
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""                  int : node
        hashtable = {1:(1), 3:(3)}          ()
        
        hashmap = {   int      ObjectRef
        
                        1    :  Obje3dxvfsfwfqfqqq (1:1)
                        2    :  Obersres(2:2)
        
        }
        
        
        
        freq =      {1:3, 3:4}
        
        count = 4
        
        cap = 5 , 1:1, 2:2,  get(1),   3:3, 4:4, get(3) , 5:5. get(4)
        
      h                       t
     (d) (2) (1)
              t
         ptr
""" 
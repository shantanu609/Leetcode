class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.array = [] 

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.d:
            return False 
        
        index = len(self.array)
        self.array.append(val)
        self.d[val] = index 
        return True 

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.d:
            return False 
        
        index = self.d[val]
        lastElement = self.array[-1]
        self.array[index], self.array[-1] = self.array[-1], self.array[index]
        self.d[lastElement] = index 
        # remove the val from dict and array 
        self.array.pop()
        self.d.pop(val)
        return True 
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
class DSU:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
    
    def find(self, num):
        if self.parent[num] != num:
            self.parent[num] = self.find(self.parent[num])
        
        return self.parent[num]

    def union(self, num1, num2):
        self.parent[self.find(num1)] = self.find(num2)
        
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        size = len(isConnected)
        dsu = DSU(size)
        d = {}
        count = 0
        
        for i in range(size):
            one = i 
            for j in range(len(isConnected[0])):
                
                second = j
                    
                if isConnected[one][second] == 1 and one != second:
                    dsu.union(one, second)

        
        cout = 0 
        for i in range(len(dsu.parent)):
            if dsu.parent[i] == i:
                count += 1 
            
        return count
            
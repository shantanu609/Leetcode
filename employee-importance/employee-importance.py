"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    count = None
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        visited = set()
        self.count = 0
        ds = {}
        for i in range(len(employees)):
            if employees[i].id not in ds:
                ds[employees[i].id] = [employees[i].importance, employees[i].subordinates]
                
        self._dfs(ds, id, visited)
        return self.count
    
    def _dfs(self, ds, targetID, visited):
        # base case 
        
        
        # logic 
        self.count += ds[targetID][0]
        visited.add(targetID)
        for nextId in ds[targetID][1]:
            self._dfs(ds, nextId, visited)
        
        
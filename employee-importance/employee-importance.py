"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = {} 
        for e in employees:
            d[e.id] = e 
        
        self.total = 0 
        self.recurse(id, d)
        return self.total 
    
    def recurse(self, targetId, d): 
        # base case 
        
        # logic 
        emp = d[targetId]
        self.total += emp.importance
        for sub in emp.subordinates:
            self.recurse(sub, d)
        
        
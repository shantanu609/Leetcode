# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrityCandidate = 0 
        for i in range(0, n):
            if knows(celebrityCandidate, i):
                celebrityCandidate = i 
        
        if self.isCelebrity(celebrityCandidate, n):
            return celebrityCandidate 
        
        return -1 
    
    def isCelebrity(self, i, n):
        for j in range(0, n):
            if j == i:
                continue 
            
            if knows(i, j) or not knows(j, i):
                return False 
    
        return True 
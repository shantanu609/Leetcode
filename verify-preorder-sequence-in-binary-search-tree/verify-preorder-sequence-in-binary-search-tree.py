class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = [] 
        low = float('-inf')
        
        for num in preorder: 
            if num < low: 
                return False 
        
            while stack and stack[-1] < num: 
                low = stack.pop() 
            
            stack.append(num)
        
        return True 
            
class Solution:
    def mctFromLeafValues(self, A: List[int]) -> int:
        stack = [float('inf')]
        res = 0
        
        for leaf in A: 
            while stack and stack[-1] <= leaf: 
                firstLeaf = stack.pop() 
                res = res + (firstLeaf * min(stack[-1], leaf))
            
            stack.append(leaf)
        
        while len(stack) > 2: 
            res = res + (stack.pop() * stack[-1])
        
        return res
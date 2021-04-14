class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
            pushed = [1,2,3,4,5]
                              x                                   
                                    stack = []
            popped = [4,5,3,2,1]
                                j
        """
        j = 0
        stack = []
        for num in pushed:
            stack.append(num)
            
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1 
        
        return j == len(popped)
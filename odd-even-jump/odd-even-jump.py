class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        """
            odd numbered jumps -> arr[i] < arr[j]
            
            even numbered jumps -> arr[i] >= arr[j]
            
    def oddEvenJumps(self, A):
        n = len(A)
        next_higher, next_lower = [0] * n, [0] * n

        stack = []
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        higher, lower = [0] * n, [0] * n
        higher[-1] = lower[-1] = 1
        for i in range(n - 1)[::-1]:
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]
        return sum(higher)
        
        
     arr = [10,13,12,14,15]
     
     next_higher = [2,3,3,4,0]

     next_lower = [0,2,0,0,0]
     
                                                                                           
     higher = [0, 0, 0, 1, 1]
     
     lower  = [0, 0, 0, 0, 1]
""" 
        
        even_jumps = [0] * len(arr)
        odd_jumps = [0]  * len(arr)
        stack = []
        
        for j, i in sorted([[j, i] for i,j in enumerate(arr)]):
            while stack and stack[-1] < i:
                odd_jumps[stack.pop()] = i
            
            stack.append(i)
    
        stack = [] 
        for j, i in sorted([[-j, i] for i, j in enumerate(arr)]):
            while stack and stack[-1] < i: 
                even_jumps[stack.pop()] = i 
            
            stack.append(i)
        
        odd = [0] * len(arr)
        even = [0] * len(arr)
    
        odd[-1] = even[-1] = 1
        
        for i in range(len(arr) - 2, -1, -1):
            
            odd[i] = even[odd_jumps[i]]
            even[i] = odd[even_jumps[i]]
        
        
        return sum(odd)        
        
        
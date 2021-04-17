class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []
        
        for i in range(len(T)):
            if not stack:
                stack.append((T[i], i))
            else:
                if stack[-1][0] < T[i]:
                    while stack and stack[-1][0] < T[i]:
                        temp, indx = stack.pop()
                        res[indx] = i - indx
                stack.append((T[i], i))
        
        return res
                    
                        
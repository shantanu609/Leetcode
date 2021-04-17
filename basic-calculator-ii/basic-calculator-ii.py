class Solution:
    def calculate(self, s: str) -> int:
        stack = [] 
        currOp = '+'
        currNum = 0 
        
        for i in range(len(s)):
            if s[i].isdigit():
                currNum = currNum * 10 + int(s[i])
            
            if (s[i] != ' ' and not s[i].isdigit()) or i == len(s) -1 :
                
                if currOp == '+':
                    stack.append(currNum)
                    
                elif currOp == '-':
                    stack.append(-currNum)
                    
                elif currOp == '*':
                    first = stack.pop()
                    stack.append(first * currNum)

                elif currOp == '/':
                    first = float(stack.pop())
                    stack.append(int(first / currNum))
                    
                currNum = 0 
                currOp = s[i]
        res = 0 
        while stack:
            res += stack.pop()
        
        return res
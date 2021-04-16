class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for op in tokens:
            if op != '+' and op != '-' and op != '*' and op != '/':
                stack.append(op)
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                
                if op == '+':
                    stack.append(first + second)
                
                elif op == '-':
                    stack.append(first - second)
                
                elif op == '*':
                    stack.append(first * second)
                
                elif op == '/':
                    stack.append(int(float(first)/second)) # floor division 

        return stack[0]
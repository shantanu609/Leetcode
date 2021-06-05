class Solution:
    def reformat(self, s: str) -> str:
        stackAlpha = [] 
        stackNum = [] 
        
        for index in range(len(s)):
            char = s[index] 
            
            if char.isdigit():
                stackNum.append(char)
                continue 
            
            stackAlpha.append(char)
        
#         if (stackAlpha and not stackNum) or (not stackAlpha and stackNum) or abs(len(stackAlpha) - len(stackNum) > 1):
#             return ""
        
        output = [] 
        
        while stackAlpha and stackNum:
            if len(stackAlpha) > len(stackNum):
                output.append(stackAlpha.pop())
                output.append(stackNum.pop())
            else: 
                output.append(stackNum.pop())
                output.append(stackAlpha.pop())
        
        if stackAlpha: 
            while stackAlpha: 
                if output and  output[-1].isalpha(): 
                    return ""
                output.append(stackAlpha.pop())
            
        elif stackNum: 
            while stackNum:
                if output and output[-1].isdigit():
                    return ""
                
                output.append(stackNum.pop())
            
        
        return "".join(output)
                
class Solution:
    def expand(self, s: str) -> List[str]:
        output = [""]
        chars = [] 
        mult = False 
        
        for char in s: 
            if char == ",":
                continue 
            
            if char == '{':
                mult = True 
            
            elif char == '}':
                temp = []
                for i in range(len(output)):
                    base = output[i]
                    
                    for nextChar in sorted(chars):
                        temp.append(base + nextChar) 
                
                output = temp
                
                chars = [] 
                mult = False 
            
            elif mult : 
                chars.append(char)
            
            else: 
                for i in range(len(output)):
                    base = output[i]
                    output[i] = base + char
        
        return output
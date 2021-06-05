class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        if numRows == 1 : 
            return output
        
        output.append([1,1])
        if numRows == 2: 
            return output
        
    
        while len(output) < numRows: 
            temp = [1]
            for i in range(1, len(output[-1])):
                temp.append(output[-1][i-1] + output[-1][i])
            
            temp.append(1)

            output.append(temp)
        
        return output
class Solution:
    res = None 
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return [] 
        
        self.res = [] 
        
        d = {
            '2' : 'abc', 
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        
        temp = [] 
        for ch in digits:
            temp.append(d[ch])
            
        self.backtrack(digits, d, 0, [], 0)
        return self.res 
    
    def backtrack(self, digits, d, indx, sb, limit):
        # base case 
        if limit == len(digits):
            temp = ''.join(sb)
            self.res.append(temp)
            return 
        
        # logic 
        ch = digits[indx]
        string = d[ch]
        for i in range(len(string)):
            sb.append(string[i])
            self.backtrack(digits, d, indx + 1, sb, limit+1)
            sb.pop()
        
        
        
                
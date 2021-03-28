class Solution:
    res = None 
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = [] 
        self.backtrack(n, n, [])
        return self.res 

    def backtrack(self, leftCount, rightCount, sb):
        # base case 
        if leftCount > rightCount :
            return 
        
        if leftCount == 0 and rightCount == 0:
            temp = ''.join(sb.copy())
            self.res.append(temp)
            return 
        
        # logic 
        if leftCount:
            sb.append('(')
            self.backtrack(leftCount - 1, rightCount, sb)
            sb.pop()
        
        if rightCount:
            sb.append(')')
            self.backtrack(leftCount, rightCount - 1, sb)
            sb.pop()
            
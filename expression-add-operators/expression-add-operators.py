"""  i
    "123"
 /.   /.       \.      \
1 23  1+2 '3'  1-2 '3'  1*2 '3'

     3 |"1+2"| 2
    
+2 -> head = calc + curr  | tail = curr 
-2 -> head = calc - curr  | tail = curr
*3 -> calc - tail + (tail x curr)    

"""
class Solution:
    result = None 
    def addOperators(self, num: str, target: int) -> List[str]:
        if len(num) == 0:
            return [] 
    
        self.result = [] 
        self.backtrack(num, target, [], 0, 0, 0)
        return self.result 
    
    def backtrack(self, num, target, sb, indx, head, tail):
        # base case 
        if indx == len(num):
            if head == target:
                self.result.append(''.join(sb))
                
            return 
    
        # logic 
        for i in range(indx, len(num)):
            # check for 0th index 
            # 1) check if we have a zero at the start? if yes -> do nothing 
            if num[indx] == '0' and indx != i:
                break 
                
            curr = int(num[indx: i+1])
            
            # 2) consider the first char and recurse on that -> we are doing not choose operation 
            if indx == 0:
                sb.append(str(curr))
                self.backtrack(num, target, sb, i+1, curr, curr)
                sb.pop()
            else:
                # three things 
                # 1) +
                sb.append('+')
                sb.append(str(curr))
                self.backtrack(num, target, sb, i+1, head + curr, curr)
                sb.pop()
                sb.pop()
                
                # 2) -
                sb.append('-')
                sb.append(str(curr))    
                self.backtrack(num, target, sb, i+1, head - curr, -curr)
                sb.pop()
                sb.pop()
                
                # 3) *
                sb.append('*')
                sb.append(str(curr))
                self.backtrack(num, target, sb, i+1, head - tail + (tail * curr), (tail * curr))
                sb.pop()
                sb.pop()
        

        
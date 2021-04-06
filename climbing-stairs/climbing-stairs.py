class Solution:
    def climbStairs(self, n: int) -> int:
        """
                [0,1,2,3,4,5,6]
                [0,1,2/1, ]
        """ 
        if n == 1 or n == 2 :
            return n 
        
        one = 1 
        two = 2 
        
        for i in range(2, n):
            res = one + two 
            one = two 
            two = res 
        
        return two
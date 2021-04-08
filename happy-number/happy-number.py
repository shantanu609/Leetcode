class Solution:
    def isHappy(self, n: int) -> bool:
        """
             2 
          - 4
          - 16
          - 37
          - 30
          - 9
          - 81
          - 65
          - 61
          - 37
        """
        d = set()
        while True: 
            n = self.helper(n)
            # print(n)
            if n in d:
                # print(d)
                return False 
            d.add(n)
            if n == 1:
                return True 
        
    
    def helper(self, num):
        li = []
        while num > 0:
            last = num % 10
            li.append(last)
            num = num // 10
        sq = 0 
        for n in li:
            sq += n * n 
        
        return sq
            
            
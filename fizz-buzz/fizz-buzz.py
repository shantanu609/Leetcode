class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            num = i 
            
            if num % 3 != 0 and num % 5 != 0:
                res.append(str(num))
                continue 
                
            if num % 3 == 0 and num % 5 != 0:
                res.append('Fizz')
                continue 
            
            if num % 3 != 0 and num % 5 == 0:
                res.append("Buzz")
                continue 
            
            if num % 5 == 0 and num % 3 == 0:
                res.append("FizzBuzz")
                continue 
        
        return res 
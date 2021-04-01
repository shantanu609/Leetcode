class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        one = 0 
        for ch in binary:
            if ch == '1':
                one += 1 
        
        return one
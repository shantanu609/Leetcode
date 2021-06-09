class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        self.ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        
        self.less_than_100 = ["","Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        self.thousands = ["", "Thousand", "Million", "Billion"]
        
        res = ""
        
        for i in range(len(self.thousands)):
            if num % 1000 != 0: 
                res = self.helper(num % 1000) + " " + self.thousands[i] + " " + res
            
            num = num // 1000 
        
        return " ".join(res.split())
    
    def helper(self, num):
        if num == 0:
            return ''
        
        if num < 20 : 
            return self.ones[num]
        
        if num < 100 :
            return self.less_than_100[num // 10] + " " + self.ones[num % 10]
        
        else:
            return self.ones[num // 100] + " Hundred " + self.helper(num % 100)
        
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        """
            "alice@leetcode.com"
            local name = alice 
            domain = @leetcode.com
            
            1) periods in between chars in local name --> ignore it. 
            2) '+' char in the local name --> ignore chars after it. 
        """
        
        d = {} 
        for email in emails: 
            temp = [] 
            i = 0 
            flag = False 
            while i < len(email):
                char = email[i]
                if char  =='.' and flag == False: 
                    i += 1 
                    continue 
                
                if char == '+':
                    while i < len(email) and email[i+1] != '@':
                        i += 1 
                    
                    i += 1 
                    continue
                
                if char == '@':
                    flag = True 
                    
                temp.append(char)
                i += 1 
            
            string = ''.join(temp)
            
            if string not in d:
                d[string] = 1 
    
        return len(d)
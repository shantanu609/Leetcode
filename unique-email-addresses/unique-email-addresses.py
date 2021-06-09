class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        """
        ["test.email+alex@leetcode.com",
         "test.e.mail+bob.cathy@leetcode.com",
         "testemail+david@lee.tcode.com"
         ]
        """
        d = {} 
        for email in emails: 
            j = 0 
            substring = [] 
            
            while j < len(email):
                if email[j] == '.':
                    j += 1 
                    continue 
                
                if email[j] == '+':
                    while j+1 < len(email) and email[j+1] != '@':
                        j += 1 
                    j += 1 
                    continue 
                
                if email[j] == '@':
                    substring.append(email[j:])
                    break 
                
                substring.append(email[j])
                j += 1 
            
            substring = ''.join(substring)
            if substring not in d: 
                d[substring] = [] 
            
            d[substring].append(email)

        return len(d)
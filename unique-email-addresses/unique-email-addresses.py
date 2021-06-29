class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        """
        Rules: 
        1) '.' ignore dot in local name
        2) '+' in local name -> ignore everything after + 
        
        Time = O(n x m)
        Space = O(m)
        """
        
        uniqueEmails = set()
        
        for email in emails: 
            domain = ''
            localName = []
            flag = False 
            
            for indx in range(len(email)):
                
                if email[indx] == '@':
                    domain = email[indx: ]
                    break 
                    
                if flag == True:
                    continue 
                
                if email[indx] == '.':
                    continue 
                
                if email[indx] == '+':
                    flag = True 
                    continue 
                
                localName.append(email[indx])
            
            email = ''.join(localName) + domain 
            
            if email not in uniqueEmails: 
                uniqueEmails.add(email)
        
        return len(uniqueEmails)
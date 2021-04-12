class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        d = {} 
        for indx in range(len(accounts)):
            for i in range(1, len(accounts[indx])):
                email = accounts[indx][i]
                if email not in d:
                    d[email] = set()
                d[email].add(indx)
        
        visited = [False] * len(accounts)
        output = [] 
        
        for i in range(len(visited)):
            if visited[i] == False:
                for email, array in d.items():
                    if visited[i] == False:
                        mergedSet = set()
                        self.dfs(accounts, d, visited, mergedSet, list(array))

                        mergedList = list(mergedSet)
                        mergedList.sort()
                        #               name           remaining emails in sorted order
                        if mergedList:
                            output.append([accounts[i][0]] + mergedList)

                        # mark vistied array 
                        for indx in array:
                            visited[indx] = True 
                        
        return output 
    
    def dfs(self, accounts, d, visited, mergedSet, stack):
        # base case 
        
        # logic 
        while stack:
            indx = stack.pop(0)
            if visited[indx] == False:
                visited[indx] = True 
                for i in range(1, len(accounts[indx])):
                    email = accounts[indx][i]
                    mergedSet.add(email)
                    newArray = d[email]
                    for allIndexes in newArray:
                        stack.append(allIndexes)
                
                
                
                
                
                
                
                
                
                
                
                
                
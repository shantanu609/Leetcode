from collections import deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {}
        indegree = {}
        q = deque()
        output = []
        
        for word in words:
            for char in word:
#                 if char not in graph:
#                     graph[char] = set() 
                
                if char not in indegree:
                    indegree[char] = 0 
        
        for i in range(1, len(words)):
            flag = False 
            
            firstWord = words[i-1]
            secondWord = words[i]
            
            for j in range(min(len(firstWord), len(secondWord))):
                
                if firstWord[j] != secondWord[j]:
                    flag = True 
                    
                    if firstWord[j] not in graph:
                        graph[firstWord[j]] = set() 
                    
                    if secondWord[j] not in graph[firstWord[j]]:
                        graph[firstWord[j]].add(secondWord[j])
                        indegree[secondWord[j]] += 1
                    break 
            
            if not flag:
                if len(secondWord) < len(firstWord) : 
                    return '' 
        
        for char, degree in indegree.items():
            if degree == 0:
                q.append(char)
        
        while q: 
            curr = q.popleft() 
            output.append(curr)
            if curr in graph:
                for nextNode in graph[curr]:
                    indegree[nextNode] -= 1 
                    if indegree[nextNode] == 0:
                        q.append(nextNode)
        
        # print(indegree, output)
        if len(indegree) > len(output):
            return ''

        return ''.join(output)
                    
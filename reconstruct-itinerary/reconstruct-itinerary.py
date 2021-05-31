class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        for dept, arr in tickets: 
            if dept not in graph:
                graph[dept] = [] 
            
            graph[dept].append(arr)
        
        for key in graph.keys(): 
            graph[key].sort(reverse = True)
        
        result = [] 
        stack = ["JFK"] 
        
        while len(stack) > 0: 
            lastArr = stack[-1]
            
            if lastArr in graph and graph[lastArr]:
                stack.append(graph[lastArr].pop())
            
            else:
                result.append(stack.pop())
            
            
        return result[::-1]
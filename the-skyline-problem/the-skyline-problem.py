import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        # build the data structure for the input array 
        inputArray = self._buildSkyLineStucture(buildings)
        
        pq = [0]        # heapq used only for height.
        result = [] 
        
        for x, h, start in inputArray:
            
            top = -pq[0]
            
            if start == 's':
                # check if the height is greater than the top element on the pq 
                heapq.heappush(pq, -h)
                
                if -pq[0] != top:
                    result.append([x, h])
            
            else:
                # if end point, the delete from pq and check for point. 
                pq.remove(-h)
                
                heapq.heapify(pq)
                
                if top != -pq[0]:
                    result.append([x, -pq[0]])
                
        
        return result
                
            
        

    def _buildSkyLineStucture(self, buildings):
        start = [] 
        end = [] 
        
        for x1, x2, h in buildings:
            start.append([x1, h, 's'])
            end.append([x2, h, 'e'])
        
        # sort start array based on the factor that heigher height comes first 
        start.sort(key = lambda x : (x[0], -x[1]))
    
        # sort end aray based on the factor that smaller height comes first for ending. 
        end.sort(key = lambda x : (x[0], x[1]))
        
        # merge the two array 
        start.extend(end)
        
        # again sort the start array to get one unified points based on x point 
        start.sort(key = lambda x : x[0])
        
        return start
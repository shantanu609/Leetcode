class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        indx = 0 
        output = [] 
        
        while indx < len(intervals) and intervals[indx][0] < newInterval[0]:
            output.append(intervals[indx])
            indx += 1 
        
        if not output or output[-1][1] < newInterval[0]:
            output.append(newInterval)
        
        else:
            output[-1][1] = max(output[-1][1], newInterval[1])
        
        
        while indx < len(intervals):
            interval = intervals[indx]
            start, end = interval 
            
            if output[-1][1] < start:
                output.append(interval)
                indx += 1 
                continue 
            
            output[-1][1] = max(output[-1][1] , end)
            indx += 1 
    
        return output
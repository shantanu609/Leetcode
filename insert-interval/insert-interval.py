class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = [] 
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        
        for i in range(len(intervals)):
            if not output: 
                output.append(intervals[i])
                continue 
        
            # check if overlap 
            oldstart, oldend = output[-1]
            newstart, newend = intervals[i]
            
            if oldstart <= newstart <= oldend: 
                # overlap 
                output[-1][1] = max(output[-1][1], newend)
                continue 
            
            output.append(intervals[i])
    
        return output
            
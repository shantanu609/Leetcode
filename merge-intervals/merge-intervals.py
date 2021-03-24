class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
            [[2,6], [1,3],[5,10],[15,18]]
            
        """
        intervals.sort(key = lambda x : x[0])
        start, end = intervals[0][0], intervals[0][1]
        
        mergedIntervals = []
        
        for i in range(1, len(intervals)):
            newStart, newEnd = intervals[i]
            
            if end < newStart:
                mergedIntervals.append([start, end])
                start, end = newStart, newEnd 
            else:
                # mergining condition 
                end = max(end , newEnd)
        
        mergedIntervals.append([start, end])
    
        return mergedIntervals
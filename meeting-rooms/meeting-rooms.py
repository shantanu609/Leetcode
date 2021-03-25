class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
           [[0,30], [15,20]]
                                        i 
            steps : 1) sort  = [0,30] [5,10] [15,20]
                    2) Priority Queue :- minHeap -> based on end time 
                    3) Loop :- 
                        a) entry into the pq  upon empty 
                        b) check if end time of the interval in pq <= start time of i 
                            i) poll() 
                            either ways interval to the pq 
                    4) return len(pq) == len(intervals)
            
        """
        intervals.sort(key = lambda x : x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False 
        
        return True 
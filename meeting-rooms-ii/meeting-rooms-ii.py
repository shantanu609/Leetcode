import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x :x[0] )
        pq = [] 
        
        for meeting in intervals:
            startTime, endTime = meeting 
            if not pq:
                heapq.heappush(pq, (endTime, -startTime))
            else:
                curr = pq[0]
                if startTime >= curr[0]:
                    heapq.heappop(pq)
                heapq.heappush(pq, (endTime, -startTime))
        
        return len(pq)
                
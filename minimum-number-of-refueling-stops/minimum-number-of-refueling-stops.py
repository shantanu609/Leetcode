import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
    10        stations = [[10,60],[20,30],[30,30],[60,40]]        target = 100 
                                                                             i
                                               
                
                fuel = 60 - 60 = 0 + 40 = 40 - 40 = 0 
                stops = 2
                
                dp = [0, 0, 0, 0]
        """
        
        pq = [] 
        res = 0 
        prev = 0 
        stations.append([target, float('inf')])
        
        for miles, fuel in stations: 
            startFuel = startFuel - (miles - prev)
            
            while pq and startFuel < 0:
                # choosing the stop logic
                # while we have some fuel in the tank that we can go to next gas station
                startFuel = startFuel + (-1 * heapq.heappop(pq)) 
                res += 1 
            
            # edge case : even after filling fuel at stop, if tank goes empty, we are done.
            if startFuel < 0:
                print(startFuel, miles, fuel)
                return -1 
            
            heapq.heappush(pq, -fuel)   # becase we want a max heap 
            
            # mark the last visited gas station for retroactively going back and filling. 
            prev = miles 
        
        return res
            
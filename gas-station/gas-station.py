class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        last = 0 
        curr = 0 
        res = 0 
        for i in range(len(gas)):
            last += gas[i] - cost[i]
            curr += gas[i] - cost[i]
            
            if curr < 0: 
                res = i+1 
                curr = 0 
        
        return res if last >= 0 else -1 
                
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """         0 1 2 3 4  
            gas =  [1,2,3,4,5]
            cost = [3,4,5,1,2]
         
        """
        result = -1 
        nums = []
        max_ = float('-inf')
        indexes = []
        for i in range(len(gas)):
            fuel = gas[i]-cost[i]
            if fuel >= 0:
                indexes.append(i)
            nums.append(fuel)
        
        print(nums, indexes)
        n = len(gas)
        
        for index in indexes: 
            curr = nums[index]
            for i in range(index+1, index + len(gas)+1):
                i = i % n 
                curr = curr + nums[i]
                if curr < 0 :
                    break
                
                if i == index:
                    return index
        
        return -1
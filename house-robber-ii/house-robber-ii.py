class Solution:
    def rob(self, nums: List[int]) -> int:
        """
            [2,3,3]
            leftdp = [0,0,0,0]  = [2,3,0]
            rightDp = [0,0,0,0] = [0,3,3]
          """
        if len(nums) == 1 :
            return nums[0]
        
        dpFirst = [0] * (len(nums) + 1)
        # dpFirst[-2] = nums[-]
        
        dpLast = [0]  * (len(nums) + 1)
        dpLast[-2] = nums[-1]
        
        for i in range(len(dpFirst)-3, -1, -1):
            dpFirst[i] = max(dpFirst[i+1], nums[i] + dpFirst[i+2])
        
        for i in range(len(dpLast)-3, -1, -1):
            if i == 0:
                dpLast[i] = max(dpLast[i+1], dpLast[i+2])        
            else:
                dpLast[i] = max(dpLast[i+1], dpLast[i+2]+ nums[i])
        
        print(dpFirst)
        print(dpLast)
        return max(dpFirst[0], dpLast[0])
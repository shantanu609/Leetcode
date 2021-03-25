class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        
        # initialize the dp array 
        dp[0] = 1 
        # check if starting 0th index element in our string is zero or no? it no then 1 else 0 in dp 
        dp[1] = 1 if s[0] != '0' else 0 
        
        # loop through the remaining string in s from 1 to n 
        for i in range(1, n):
            
            # check if s[i] is not zero? if not then use the current value in dp for dp[i+1]
            if s[i] != '0':
                dp[i+1] = dp[i]
                
            # check for two digits. it within this range of 10 <= __ <= 26 then add dp[i-1]
            # dont forget to check for the bound 
            if i < len(s):
                temp = int(s[i-1 : i+1])
                if 10 <= temp <= 26:
                    dp[i+1] += dp[i-1]
        
        return dp[-1]
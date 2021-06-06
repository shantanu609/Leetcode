class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # ptr1 --> s and ptr2 --> t
        ptr1 = ptr2 = 0 
        
        while ptr1 < len(s) and ptr2 < len(t):
            
            # check if character matches at both s and t 
            if s[ptr1] == t[ptr2]:
                ptr1 += 1 
                ptr2 += 1 
        
            else:
                # they are not matching, then push ptr2 ahead in search for the matching character 
                ptr2 += 1 
        
        return ptr1 == len(s)
        
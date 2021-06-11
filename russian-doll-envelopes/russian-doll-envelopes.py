import bisect 
class Solution:
    def maxEnvelopes(self, en: List[List[int]]) -> int:
        en.sort(key = lambda x : (x[0], -x[1]))
                
        tail = []
        
        for i in range(len(en)):
                height = en[i][1]
                indx = bisect.bisect_left(tail, height)
                
                if indx >= len(tail):
                    tail.append(height)
                else:
                    tail[indx] = height 
        
        print(tail)
        return len(tail)
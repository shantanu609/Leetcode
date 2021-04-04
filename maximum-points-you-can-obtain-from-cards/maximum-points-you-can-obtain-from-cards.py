class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints)
        
        left = [0] * (k+1)
        right = [0] * (k+1)
        
        for i in range(1, k+1):
            left[i] = left[i-1] + cardPoints[i-1]
        
        for i in range(1, k+1):
            right[i] = right[i-1] + cardPoints[len(cardPoints)-i]
        
        res = 0 
        
        for i in range(0, k+1):
            total = left[i] + right[k-i]
            res = max(res, total)
        
        return res
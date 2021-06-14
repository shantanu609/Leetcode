# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, nums: List[int]) -> int:
        node = head 
        d = {} 
        res = 0 
        for num in nums:
            d[num] = 1 
            
        while node: 
            
            if node.val in d: 
                res += 1 
                prev = node 
                
                while prev and prev.val in d: 
                    prev = prev.next 
                
                node = prev 
            
            if node:
                node = node.next 
        
        return res
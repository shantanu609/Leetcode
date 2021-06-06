# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node = head 
        num = 0 
        
        while node: 
            num = num * 10 + node.val
            node = node.next
        
        
        result = int(str(num), 2)
        
        return result
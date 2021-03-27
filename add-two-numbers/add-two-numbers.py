# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0 
        dummy = ListNode(-1)
        node = dummy 
        
        while l1 and l2: 
            s = l1.val + l2.val + carry 
            nodeval = s % 10 
            carry = s // 10 
            node.next = ListNode(nodeval)
            node = node.next 
            l1 = l1.next 
            l2 = l2.next 
        
        l1 = l1 if l1 else l2 
        while l1:
            s = l1.val + carry 
            nodeval = s % 10 
            carry = s // 10 
            node.next = ListNode(nodeval )
            node = node.next 
            l1 = l1.next 
        
        if carry:
            node.next = ListNode(carry)
        return dummy.next 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head 
        
        odd = head 
        even = head.next 
        l1 = odd 
        l2 = even 
        
        while l1.next and l2.next: 
            l1.next = l2.next 
            l2.next = l2.next.next 
            l1 = l1.next 
            l2 = l2.next 
        
        if l1: 
            l1.next = even 
            return odd 
        
        else: 
            l1 = odd 
            while l1.next: 
                l1 = l1.next 
            
            l1.next = even 
        
            return odd
            
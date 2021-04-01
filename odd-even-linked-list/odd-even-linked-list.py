# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head 
        odd = node1 = head 
        even = node2 = head.next 
        
        while node1 and node1.next or node2 and node2.next:
            node1.next = node1.next.next 
            node1 = node1.next 
            if node2.next :
                node2.next = node2.next.next 
                node2 = node2.next 
        
        while odd and odd.next: 
            odd = odd.next 
        
        odd.next = even 
    
        return head
        
        
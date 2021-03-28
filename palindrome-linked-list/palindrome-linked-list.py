# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """ p1                  p2 
            7 -> 6 -> 8 -> 9 -> 7 -> 6 -> 8
            7 -> 6 -> 8 
                                
        """
        slow  = head 
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        slow.next = self.reverse(slow.next)
        p1 = head 
        p2 = slow.next 
        
        while p2: 
            if p1.val != p2.val:
                return False 
            p1 = p1.next 
            p2 = p2.next 
        
        return True 

    def reverse(self, node):
        prev = None 
        while node:
            nodeNext = node.next 
            node.next = prev 
            prev = node 
            node = nodeNext 
        
        return prev 
            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq # min
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
            lists = [[1,4,5],[1,3,4],[2,6]]
            
            
            heap = [ (4, 0, (5)), (3, 1, (4)) , (2, 2, (6))  ]
            
            dummy -> Node(1) -> Node(1) -> 
        """
        pq = [] 
        
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(pq, (lists[i].val, i, lists[i].next))
        
        dummy = ListNode(-1)
        curr = dummy
        
        while pq:
            val, index, node = heapq.heappop(pq)
            curr.next = ListNode(val)
            curr = curr.next 
            
            if node:
                heapq.heappush(pq, (node.val, index, node.next))
        
        return dummy.next
            
        
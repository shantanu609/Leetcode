# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = [] 
        dummy = ListNode(-1)
        node = dummy
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(pq, (lists[i].val, i, lists[i]))
        
        while pq:
            val, index, curr = heapq.heappop(pq)
            node.next = curr
            node = node.next 
            curr = curr.next
            if curr:
                heapq.heappush(pq, (curr.val, index, curr))
        
        return dummy.next
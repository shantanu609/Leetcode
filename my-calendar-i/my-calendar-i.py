class ListNode: 
    def __init__(self, start, end):
        self.start = start 
        self.end = end 
        self.left = None 
        self.right = None 
    
    def _insert(self, node):
        if node.start >= self.end: 
            if not self.right:
                self.right = node 
                return True 
            
            return self.right._insert(node)
        
        elif node.end <= self.start:
            if not self.left:
                self.left = node 
                return True 
            
            return self.left._insert(node)
        
        else:
            return False 
        
class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = ListNode(start, end)
            return True 
        
        newNode = ListNode(start, end)
        
        return self.root._insert(newNode)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
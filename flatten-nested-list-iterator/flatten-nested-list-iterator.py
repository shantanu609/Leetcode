# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    stack = None 
    cursor = None 
    def __init__(self, nestedList: [NestedInteger]):
        
        # 1) Create a stack for storing all the iteators.  
        self.stack = [] 
        
        # 2) append all iterators
        if nestedList:
            self.stack.append(iter(nestedList))

    
    def next(self) -> int:
        # Save the cursor value because the value cannot be same for each next function call.
        value = self.cursor 
        self.cursor = None 
        return value 
    
    def hasNext(self) -> bool:
        while self.stack and self.cursor == None:
            
            iterator = self.stack[-1]
            temp = next(iterator,None)
            
            if temp == None: # that means there is not next 
                self.stack.pop()
                continue
            
            nestedInt = temp 
            
            if temp.isInteger():
                self.cursor = nestedInt.getInteger() 
                return True 
            else:
                self.stack.append(iter(nestedInt.getList()))
        
        return False
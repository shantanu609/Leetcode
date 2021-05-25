# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root 
        self.arr = []
        self._getInorder(root)
        self.ptr = 0 

    def next(self) -> int:
        nextNode = self.arr[self.ptr]
        self.ptr += 1 
        return nextNode.val
    
    def hasNext(self) -> bool:
        if self.ptr < len(self.arr):
            return True 
        
        return False 
    
    def _getInorder(self, root):
        if root:
            self._getInorder(root.left)
            self.arr.append(root)
            self._getInorder(root.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root 
        self.root.val = 0 
        self.d = {0:0} 
        self._recover(self.root)
        
    def _recover(self, root):
        # base case 
        if not root:
            return 
        
        if root.left:
            root.left.val = root.val * 2 + 1 
            self.d[root.left.val] = 1 
            self._recover(root.left)

        if root.right: 
            root.right.val = root.val * 2 + 2
            self.d[root.right.val] = 1 
            self._recover(root.right)
        
        
    def find(self, target: int) -> bool:
        if target not in self.d:
            return False 
        
        return True 


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
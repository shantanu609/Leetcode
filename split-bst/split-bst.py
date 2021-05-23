# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: TreeNode, target: int) -> List[TreeNode]:
        if not root:
            return [None, None]
        
        result = [None, None]
        return self.recursiveHelper(root, target, result)
    
    def recursiveHelper(self, root, target, result):
        # base case 
        if not root:
            return result
        
        # logic
        if root.val <= target:
            # search in right half or if equal store it in left sub tree
            result = self.recursiveHelper(root.right, target, result)
            root.right = result[0]
            result[0] = root
            return result
            
        
        else:
            # search in left half
            result = self.recursiveHelper(root.left, target, result)
            root.left = result[1]
            result[1] = root
            return result 


"""
    If I see my result array : [left_sub_tree, right_sub_tree] 
    left_sub_tree will have values less than or equals to.
    right_sub_tree will have values greater than the target.
"""
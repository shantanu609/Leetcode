# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        string = self._sHelper(root, '')
        return string
    
    def _sHelper(self, root, string):
        if not root:
            string += 'None,'
        else:
            string += str(root.val) +','
            string = self._sHelper(root.left, string)
            string = self._sHelper(root.right, string)
        
        return string

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        preorder = data.split(',')
        print(preorder)
        root = self._dHelper(preorder)
        return root
    
    def _dHelper(self, preorder):
        # base case 
        if preorder[0] == "None":
            preorder.pop(0)
            return None 
            
        # logic
        root = TreeNode(int(preorder[0]))
        preorder.pop(0)
        
        root.left = self._dHelper(preorder)
    
        root.right = self._dHelper(preorder) 
        
        return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
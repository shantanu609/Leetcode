# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        stringArr = self._sHelper(root, [])
        print("serialized string = ", stringArr)
        return ''.join(stringArr)
    
    def _sHelper(self, root, stringArr):
        # base case 
        if not root:
            stringArr.append("None,")
            return stringArr
        
        # logic 
        stringArr.append(str(root.val) + ',') 
        stringArr = self._sHelper(root.left, stringArr)
        stringArr = self._sHelper(root.right, stringArr)
        
        return stringArr
        
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        preorder = data.split(',')
        preorder.pop()
        print("preorder = ", preorder)
        root = self._dHelper(preorder)
        return root 
    
    def _dHelper(self, preorder):
        # base case 
        if len(preorder) == 0:
            return None 
         
        # logic 
        root = None
        if preorder[0] != 'None':
            root = TreeNode(preorder[0])
        
        indx = 1 
        while indx < len(preorder):
            if preorder[indx] == 'None':
                indx += 1 
                continue 
            
            if int(preorder[0]) > int(preorder[indx]):
                indx += 1 
            else:
                break
        
        if root:
            root.left = self._dHelper(preorder[1 : indx])
        if root:
            root.right = self._dHelper(preorder[indx : ])
        
        
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
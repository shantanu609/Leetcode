# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """             i
            preorder = [3,9,20,15,7]
             inorder = [9,3,15,20,7]
            
        """
        # process the inorder. Keep the node as key and value as its index
        d = {}
        for i in range(len(inorder)):
            d[inorder[i]] = i 
        
        # process the preorder and construct the tree
        root = None 
        curr = None 
        stack = []
        
        for i in range(len(preorder)):
            newNode = TreeNode(preorder[i])
            
            # check if we have a root. If not then mark the new-node as our root and add it to stack
            if not root:
                root = newNode
                stack.append(newNode)
            
            else:
                # check if we can place our newNode to the left our last processed new-node
                if stack and d[stack[-1].val] > d[newNode.val]:
                    stack[-1].left = newNode
                    stack.append(newNode)
                
                else:
                    # check where we need to put our new-node to whose right?
                    while stack and d[stack[-1].val] < d[preorder[i]]:
                        curr = stack.pop()
                    
                    curr.right = newNode
                    stack.append(newNode)
        
        return root
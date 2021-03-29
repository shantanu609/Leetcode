# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums, left, right):
        # base case 
        if left > right:
            return 
        
        # get middle 
        mid = (left + right) // 2 
        if (left+right)% 2 == 1:
            mid += 1 
        
        # return root 
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, left, mid - 1)
        node.right = self.helper(nums, mid + 1, right)
        
        return node
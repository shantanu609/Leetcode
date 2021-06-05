# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # edge case 
        if not nums:
            return None 
        
        return self.helper(nums)
    
    def helper(self, nums):
        # base case
        if len(nums) == 0:
            return None 
        
        # logic
        left, right = 0, len(nums) - 1
        mid = (left + right) // 2
        
        root = TreeNode(nums[mid])
        root.left = self.helper(nums[:mid])
        root.right = self.helper(nums[mid + 1: ])
        
        return root 
"""
        m
[-10,-3,0,5,9]

 m
[1,3]
"""
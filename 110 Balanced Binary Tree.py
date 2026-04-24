# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def subTreehight(root) -> int:
            if root == None:
                return 0
            
            return max(subTreehight(root.left) + 1, subTreehight(root.right) + 1)
        
        if root == None:
            return True
        
        left = subTreehight(root.left)
        right = subTreehight(root.right)
        
        if abs(left - right) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
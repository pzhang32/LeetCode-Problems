# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        root_val = root.val

        def checkRootVal(root, min, max) -> bool:
            if root == None:
                return True
            if min is not None:
                if root.val <= min:
                    return False
            if max is not None:
                if root.val >= max:
                    return False
            
            return checkRootVal(root.left, min, root.val) and checkRootVal(root.right, root.val, max)
        return checkRootVal(root.left, min = None, max = root_val) and checkRootVal(root.right, min = root_val, max = None)
        
        
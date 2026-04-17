# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        def compare(left_node, right_node) -> bool:
            if left_node == None and right_node == None:
                return True
            elif left_node == None or right_node == None:
                return False
            elif left_node.val == right_node.val:
                return compare(left_node.left, right_node.right) and compare(left_node.right, right_node.left)
            else:
                return False
            
        return compare(root.left, root.right)

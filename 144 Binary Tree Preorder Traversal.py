# method 1: recursion
# this method is prefered

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []

        def preorder(root: Optional[TreeNode]):
            if root == None:
                return
            lst.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return lst
    

# method 2: iteration
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []

        if root == None:
            return []
        
        stack.append(root)

        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result
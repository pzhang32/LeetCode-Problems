# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def nodeDepth(root) -> int:
            nonlocal max_depth
            if root == None:
                return 0
            else:
                left_depth = nodeDepth(root.left)
                right_depth = nodeDepth(root.right)
                max_depth = max(max_depth, left_depth + right_depth)

                return max(left_depth, right_depth) + 1
        
        nodeDepth(root)
        
        return max_depth

# 写法二，将ans定义为对象属性self.ans，内层函数可以直接修改
# def diameterOfBinaryTree(self, root):
#     self.ans = 0
    
#     def dfs(node):
#         if not node:
#             return 0
#         left = dfs(node.left)
#         right = dfs(node.right)
#         self.ans = max(self.ans, left + right)
#         return max(left, right) + 1
    
#     dfs(root)
#     return self.ans
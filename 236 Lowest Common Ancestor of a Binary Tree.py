# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 一、递归先写终止条件：
        # 遍历到空节点返回None
        if root == None:
            return root
        # 遇到目标节点返回
        if root == p or root == q:
            return root
        # 二、递归：分别从左右子树寻找目标
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 三、处理结果：
        # 左右子树都返回结果，则该节点是LCA
        if left and right:
            return root
        # 左子树找到了目标，右子树没有
        elif left and (right == None):
            return left
        # 右子树找到了目标，左子树没有
        elif right and (left == None):
            return right
        # 目标不在当前子树里
        else:
            return None
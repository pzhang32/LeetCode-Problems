# method 1: recursion


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []

        def inorder(root: Optional[TreeNode]):
            if root == None:
                return
            
            inorder(root.left)
            lst.append(root.val)
            inorder(root.right)

        inorder(root)

        return lst


# method 2 iteration
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        # 这两句是多余的，因为root是None，则直接返回空的result
        #if root == None:
            #return []

        while root or stack:
            # 如果节点存在就压栈，然后左走
            if root:
                stack.append(root)
                root = root.left    #最后这个节点会变成None，然后进入else
            # 如果节点是None
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right

        return result
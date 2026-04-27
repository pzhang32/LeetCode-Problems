# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = []
        queue.append((root, 1))
        max_with = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node, index = queue.pop(0)
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))

                if i == 0:
                    left = index
                if i == size - 1:
                    right = index
                
            width = (right - left) +1
            max_with = max(max_with, width)

        return max_with
            

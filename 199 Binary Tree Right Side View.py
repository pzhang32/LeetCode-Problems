# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        result = []
        queue.append(root)
        
        if root == None:
            return []
        
        while queue:
            inter_result = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                inter_result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(inter_result[-1])

        return result
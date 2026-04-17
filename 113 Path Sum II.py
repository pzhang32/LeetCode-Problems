# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        interList = []
        result = []
        self.pathList(root, interList, result, targetSum)
        
        return result
    
    def pathList(self, root, interList, result, targetSum):
        if root == None:
            return
        
        interList.append(root.val)
        targetSum  -= root.val

        if root.left == None and root.right == None:
            if targetSum == 0:
                result.append(interList[:])
            
        else:
            self.pathList(root.left, interList, result, targetSum)
            self.pathList(root.right, interList, result, targetSum)

        interList.pop()

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def addNode(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            if preorder == [] or inorder == []:
                return None
        
            root = TreeNode()
            root.val = preorder.pop(0)
            left = []
            right = []

            # idx = inorder.index(root.val)     # 直接找分割点
            # left = inorder[:idx]
            # right = inorder[idx + 1:]
            # 这个方法可以直接分割，如果不会的话就只能用for循环了
            
            flag = 0
            for num in inorder:
                if num == root.val:
                    flag = 1
                if flag == 0:
                    left.append(num)
                elif flag == 1 and num == root.val:
                    continue
                else:
                    right.append(num)
            
            root.left = addNode(preorder, left)
            root.right= addNode(preorder, right)

            return root

        return addNode(preorder, inorder)
    
    # 时间复杂度：O(n²) 速度会很慢，但是能通过
# 方法一，通过累加和目标做比较

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 思路：路径上节点数值累加，比较是否等于目标值
        sum = 0 #sum需要累加所以不能参与递归，不然每次递归sum都会变成从0开始
        # 因为sum不能参与递归，所以这里需要借助辅助函数
        def addCurrentSum(root, sum):
            # 判断是否是空二叉树
            if root == None:
                # 因为hasPathSum的返回值是 bool，所以这里很容易想到同样返回bool
                # 常见的设计模式是递归的辅助函数会返回和原函数同样类型的值
                return False
            # 通用情况：节点的值参与累加
            sum += root.val
            # 终止情况：在叶子节点处判断节点数值总和是否和目标值相等
            if root.left is None and root.right is None:
                if targetSum == sum:
                    return True
                else:
                    return False
            # 递归，or表示只要有一条路径符合就返回True
            return addCurrentSum(root.left, sum) or addCurrentSum(root.right, sum)
        # 使用辅助递归函数        
        return addCurrentSum(root, sum)


# 方法二：通过每次将目标值减去节点值，对最终结果是否为0进行判断
# 此方法的优点是不用写辅助递归函数
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root ==  None:
            return False

        targetSum -= root.val
        if root.left == None and root.right == None:
            if targetSum == 0:
                return True
            else:
                return False
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

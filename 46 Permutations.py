# 回溯法晦涩难懂，不如按照模板套路来写
# def backtrack(当前状态, 剩余选择):
#     if 终止条件:
#         收集结果
#         return
    
#     for 选择 in 剩余选择:
#         做选择
#         backtrack(新状态, 新剩余选择)
#         撤销选择

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        def backtrack(current, nums):
            if len(nums) == 0:
                result.append(current[:])
                return
            
            for i in range(len(nums)):
                current.append(nums[i])
                nums.pop(i)
                backtrack(current, nums)
                nums_i = current.pop()
                nums.insert(i, nums_i)

        backtrack(current, nums)

        return result
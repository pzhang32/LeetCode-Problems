# 这题AI给提示我也不会

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
    
        def backtrack(index, current):
            if index == len(nums):
                result.append(current)
                return
            
            backtrack(index + 1, current + [nums[index]])
            backtrack(index + 1, current)
        
        backtrack(0, [])
        return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    s = Solution()
    print(s.subsets(nums))


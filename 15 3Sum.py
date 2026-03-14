# 思路：排序 + 双指针
# 坑：找到解后要先跳过重复再移指针，顺序不能反

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) -1
            while left < right:
                solution = nums[i] + nums[left] + nums[right]
                if solution == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right - 1]:
                        right = right - 1
                    left = left + 1
                    right= right -1
                elif solution < 0:
                    left = left + 1
                else: right= right -1 
        return result


# test
if __name__ == "__main__":
    
    sol = Solution()
    # test example
    print(sol.threeSum([-1, 0, 1]))        # expected: [[-1, 0, 1]]
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))  # expected: [[-1,-1,2],[-1,0,1]]
    print(sol.threeSum([0, 0, 0]))         # expected: [[0,0,0]]
    print(sol.threeSum([1, 2, 3]))         # expected: []
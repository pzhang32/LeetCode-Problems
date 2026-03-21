#暴力解法，O(n³)，会超时
class Solution_ver1:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                if nums1[i] == nums2[j]:
                    sub_result = 1
                    sub_i = i + 1
                    sub_j = j + 1
                    while (sub_i < len(nums1)) and (sub_j < len(nums2)) and nums1[sub_i] == nums2[sub_j]:
                        sub_i += 1
                        sub_j += 1
                        sub_result += 1
                    result = max(result, sub_result)
        
        return result

#动态规划（Dynamic Programming，DP）
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        dp = [[0] * len(nums2) for i in range(len(nums1))]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0

        result = max(max(row) for row in dp)
        return result
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.findLength([1,2,3,2,1], [3,2,1,4,7]))   #expected Output: 3
    print(solution.findLength([0,0,0,0,0], [0,0,0,0,0]))   #expected Output: 5
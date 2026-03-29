class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_table = {}
        count = 0
        for num in nums:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 0
        
        for num in hash_table:
            if (num-1) in hash_table:
                continue
            else:
                count_temp = 0
                for i in range(len(nums)):
                    if (num+i) in hash_table:
                        count_temp += 1
                    else: break
                if count_temp > count:
                    count = count_temp

        return count
    
# 用set代码更简洁
# 这里不用计数，只需要判断某数是否存在，所以用set更好
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        count = 0

        for num in nums_set:
            if (num - 1) in nums_set:
                continue
            else:
                temp_count = 0
                while (num + temp_count) in nums_set:
                    temp_count += 1
                if temp_count > count:
                    count = temp_count
                
        return count


if __name__ == "__main__":
    s = Solution()
    nums = [100,4,200,1,3,2]
    print(s.longestConsecutive(nums))   #Expected Output: 4
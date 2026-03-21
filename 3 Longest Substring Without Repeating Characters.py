#思路：不定长度窗口，哈希表
#注意左边指针往右移动时左指针左边的内容依然是留在哈希表里的！
#所以是left = max(left, char_index[s[right]] + 1)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        result = 0
        
        for right in range(0, len(s)):
            if s[right] in char_index:
                left = max(left, char_index[s[right]] + 1)

            char_index[s[right]] = right       
            result = max(result, (right-left+1))

            #print(s[left:right+1])
            #print("left:",left," right:",right)
            #print(result)
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))   #expected Output: 3
    print(solution.lengthOfLongestSubstring("bbbbb"))   #expected Output: 1
    print(solution.lengthOfLongestSubstring("pwwkew"))   #expected Output: 3
    print(solution.lengthOfLongestSubstring("abba"))    #expected Output: 2
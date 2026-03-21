#思路：不定长度窗口，哈希表
#每次左侧指针移动一格

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        right = 0
        result = 0
        while right < len(s):
            if s[right] in char_index:
                char_index[s[right]] += 1
                while char_index[s[right]] > 1:
                    char_index[s[left]] -= 1
                    left += 1
            else:
                char_index[s[right]] = 1

            result = max(result, (right-left+1))
            right += 1
        
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))   #expected Output: 3
    print(solution.lengthOfLongestSubstring("bbbbb"))   #expected Output: 1
    print(solution.lengthOfLongestSubstring("pwwkew"))   #expected Output: 3
    print(solution.lengthOfLongestSubstring("abba"))    #expected Output: 2
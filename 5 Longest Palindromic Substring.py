class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            odd = self.expend(i, i, s)
            even = self.expend(i, i+1, s)
            if len(result) < len(odd):
                result = odd
            if len(result) < len(even):
                result = even
        
        return result

    def expend(self, left: chr, right: chr, s: str) -> str:
        result = ""
        while (left >= 0) and (right < len(s)):
            if s[left] == s[right]:
                result = s[left:right+1]
                left -=1
                right += 1
            else: break
        
        return result

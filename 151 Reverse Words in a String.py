# 这个方法思路是对的，但代码写的不够好
class Solution:
    def reverseWords(self, s: str) -> str:
        s = self.removeExtraSpace(s)
        #print("s:", s)
        result = ""
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                j = i + 1
                while j < len(s) and s[j] != " ":
                    result += s[j]
                    j += 1
                result += " "
            if i == 0 and s[i] != " ":
                j = i
                while j < len(s) and s[j] != " ":
                    result += s[j]
                    j += 1
                result += " "
            else:
                continue
        result =  result[:-1]

        return result
    
    def removeExtraSpace(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            if s[i] != " ":
                result += s[i]
            elif i != 0 and s[i] == " " and (i+1 < len(s)) and s[i+1] != " ":
                result += s[i]
            else: continue
        return result


# 第一个写的不够简洁，试着简化一下
class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        for i in range(len(s)-1, -1, -1):
            if i == len(s) - 1 and s[i] == " ": #末尾是空格的特例
                continue
            elif s[i] == " " and s[i+1] != " ": #普通的中间段的单词起始位置
                j = i + 1
                while j < len(s) and s[j] != " ":
                    result += s[j]
                    j += 1
                result += " "
            elif i == 0 and s[i] != " ":    #顶端不是空格的特例
                j = i
                while j < len(s) and s[j] != " ":
                    result += s[j]
                    j += 1
                result += " "
            else: continue  #连续空格或连续字符
        result =  result[:-1]

        return result

# 还有一行代码搞定的方法
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
        #return " ".join(s.split()[::-1])   #或者这样写


if __name__ == "__main__":
    result = Solution()

    s = "the sky is blue"
    #s = "  hello world  "
    print(result.reverseWords(s))
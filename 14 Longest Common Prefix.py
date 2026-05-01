class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        if len(strs) == 1:
            return strs[0]
        
        min_len = len(strs[0])
        for i in range(len(strs)):
            min_len = min(min_len, len(strs[i]))

        for j in range(min_len):
            for i in range(len(strs) - 1):
                # 字符串可以直接用下标访问字符，不需要事先将strs转换为二维数组
                if strs[i][j] == strs[i+1][j]:
                    continue
                else:
                    return res
            
            res += strs[i][j]

        return res
    

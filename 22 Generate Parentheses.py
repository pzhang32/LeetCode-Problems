class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        current = []
        left = n
        right = n

        def backtrace(current, left, right):
            if len(current) == 2 * n:
                result.append(''.join(current))
                return
            
            if left > 0:
                current.append("(")
                left -= 1
                backtrace(current, left, right)
                current.pop()
                left += 1
            if left < right:
                current.append(")")
                right -= 1
                backtrace(current, left, right)
                current.pop()
                right += 1

        backtrace(current, left, right)

        return result
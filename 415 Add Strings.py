#思路：分离双指针

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        while i >= 0 and j >= 0:
            n1 = ord(num1[i]) - ord("0")
            n2 = ord(num2[j]) - ord("0")
            r = (n1 + n2 + carry) % 10
            carry = (n1 + n2 + carry) // 10
            result = str(r) + result

            if i ==0 and j == 0 and carry == 1:
                result = str(carry) + result
                carry = 0
            i = i - 1
            j = j - 1

        if i < 0:
            while j >= 0:
                result = str((ord(num2[j]) - ord("0") + carry) % 10) + result
                carry = (ord(num2[j]) - ord("0") + carry) // 10
                j = j - 1
        if j < 0:
            while i >= 0:
                result = str((ord (num1[i]) - ord("0") + carry) % 10) + result
                carry = (ord (num1[i]) - ord("0") + carry) // 10
                i = i - 1

        if carry == 1:
            result = str(carry) + result


        return result



if __name__ == "__main__":

    s = Solution()

    print(s.addStrings("11", "123"))    #expected Output: "134"
    print(s.addStrings("456", "77"))    #expected Output: "533"
    print(s.addStrings("0", "0"))       #expected Output: "0"
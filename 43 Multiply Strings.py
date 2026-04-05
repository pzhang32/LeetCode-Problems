class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        lst1 = [int(num) for num in num1]
        lst2 = [int(num) for num in num2]
        lst1.reverse()
        lst2.reverse()
        #print("list1", lst1)
        #print("list2", lst2)

        carry = 0
        result = [0] * (len(lst1) + len(lst2))
        #print("res all 0:", result)
        i = 0
        j = 0
        for int1 in lst1:
            for int2 in lst2:
                res = (int1 * int2 + carry + result[i+j]) % 10
                carry = (int1 * int2 + carry + result[i+j]) // 10
                result[i+j] = res
                #print("inter result:", result)
                j += 1
            if carry != 0:
                result[i+j] += carry
                #print("first carry result:", result)
            i += 1
            j = 0
            carry = 0

        result.reverse()
        if result[0] == 0:
            result = result[1:]

        #print("reversed result:", result)
        res_str = ""
        for num in result:
            res_str += str(num)
        #print("res_str:", res_str)
        return res_str

if __name__ == "__main__":
    num1 = "99"
    num2 = "99"
    s = Solution()
    print(s.multiply(num1, num2)) #Output: "56088"
        
        
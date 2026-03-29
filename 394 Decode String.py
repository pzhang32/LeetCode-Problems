class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        current_str = ''
        lst = []
        
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                lst.append((current_str, num))
                current_str = ''
                num = 0
            elif ch == "]":
                prev_str, repeat = lst.pop()
                #print('prev_str:', prev_str, 'repeat:', repeat)
                current_str = prev_str + current_str * repeat
            else:
                current_str += ch

        return current_str


# 不熟悉元组，改用两个list来做
class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        current_str = ""
        char_stack = []
        num_stack = []

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                # push the number and string before the "["
                # when meet the "]", poped out as previous number and string
                num_stack.append(num)
                num = 0
                char_stack.append(current_str)
                current_str = ""
            elif ch == "]":
                prev_num = num_stack.pop()
                prev_str = char_stack.pop()
                current_str = prev_str + current_str * prev_num
            else:
                current_str += ch
            
        return current_str
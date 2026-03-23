#方法一：有点蠢

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_point = head
        right_point = head
        for i in range(left-1):
            left_point = left_point.next
        for j in range(right-1):
            right_point = right_point.next
        
        while left < right:
            temp = left_point.val
            left_point.val = right_point.val
            right_point.val = temp
            left += 1
            right -= 1
            left_point = left_point.next
            right_point = head
            
            for j in range(right-1):
                right_point = right_point.next

        return head
        
#方法二：减少了一个循环
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp_point = head
        for i in range(left-1):
            temp_point = temp_point.next

        start_point =  temp_point
        temp_list = []

        for j in range(right-left+1):
            temp_list.append(temp_point.val)
            temp_point = temp_point.next
        
        temp_list.reverse()

        for j in range(right-left+1):
            start_point.val = temp_list[j]
            start_point = start_point.next

        return head
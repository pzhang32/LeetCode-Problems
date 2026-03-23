#方法一：能通过，但不是出题者的本意

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        point = head
        value = []
        while point:
            value.append(point.val)
            point = point.next

        reversed_value = value[::-1]
        
        return reversed_value == value
        

#方法二：快慢指针找到链表中点，然后反转后半段，再和前半段逐一比较
# 出题者的本意

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next 
        
        cur = slow.next
        pre = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur= nxt
        while pre:
            if pre.val == head.val:
                pre = pre.next
                head = head.next
            else:
                return False
        
        return True


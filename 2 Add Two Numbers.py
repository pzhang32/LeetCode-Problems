# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        point1 = l1
        point2 = l2
        head = ListNode(0)
        carry = 0
        curr = head

        while point1 and point2:
            nxt = ListNode(0)
            value = (point1.val + point2.val + carry) % 10
            nxt.val = value
            carry = (point1.val + point2.val + carry) // 10
            point1 = point1.next
            point2 = point2.next
            curr.next = nxt
            curr = curr.next
        
        while point1:
            nxt = ListNode(0)
            value = (point1.val + carry) % 10
            nxt.val = value
            carry = (point1.val + carry) // 10
            point1 = point1.next
            curr.next = nxt
            curr = curr.next
        
        while point2:
            nxt = ListNode(0)
            value = (point2.val + carry) % 10
            nxt.val = value
            carry = (point2.val + carry) // 10
            point2 = point2.next
            curr.next = nxt
            curr = curr.next

        if carry == 1:
            nxt = ListNode(1)
            curr.next = nxt
            curr = curr.next
        
        return head.next
    

# 更简洁的写法，但是思路是一样的
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return head.next
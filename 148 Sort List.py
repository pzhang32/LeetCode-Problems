# 方法一：能通过，但不是出题人的意图
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        cur = head
        while cur:
            values.append(cur.val)
            cur = cur.next
        values.sort()

        cur = head
        for value in values:
            cur.val = value
            cur = cur.next

        return head
    
# 方法二：归并排序，递归
# 链表排序通常选用归并排序，并结合递归的方式
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.mergeList(left, right)

    def mergeList(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        result = dummy

        while left and right:
            if left.val <= right.val:
                dummy.next = left
                left = left.next
            else:
                dummy.next = right
                right = right.next
            dummy = dummy.next

        while left:
            dummy.next = left
            left = left.next
            dummy = dummy.next

        while right:
            dummy.next = right
            right = right.next
            dummy = dummy.next

        return result.next


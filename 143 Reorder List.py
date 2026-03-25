#思路：慢指针找中点，断开，后半段反转，交替合并

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head
        slow = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None

        pre = None
        while mid:
            nxt = mid.next
            mid.next = pre
            pre = mid
            mid = nxt
        
        left = head
        right = pre
        while left and right:
            nxt = left.next
            left.next = right
            right = right.next
            left.next.next = nxt
            left = nxt
        
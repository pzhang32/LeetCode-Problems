#思路：遇到head要删除的情况，应该建立一个dummy指向head，最后返回dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                while cur.next.next.next and (cur.next.next.val == cur.next.next.next.val):
                    cur.next.next = cur.next.next.next
                cur.next = cur.next.next.next
            else:
                cur = cur.next

        return dummy.next
    


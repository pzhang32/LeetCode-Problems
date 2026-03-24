# 思路：遇到链表排序通常用归并排序

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        result = dummy
        point1 = list1
        point2 = list2
        while point1 and point2:
            if point1.val <= point2.val:
                dummy.next =  point1
                point1 = point1.next
            else:
                dummy.next =  point2
                point2 = point2.next
            dummy = dummy.next

        while point1:
            dummy.next =  point1
            point1 = point1.next
            dummy = dummy.next

        while point2:
            dummy.next =  point2
            point2 = point2.next
            dummy = dummy.next

        return result.next
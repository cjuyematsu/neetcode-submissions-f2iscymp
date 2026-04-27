# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy

        while list1 or list2:
            if not list2 or (list1 and list1.val < list2.val):
                cur.next = ListNode(list1.val)
                list1 = list1.next

            else:
                cur.next = ListNode(list2.val)
                list2 = list2.next
            
            cur = cur.next
        

        return dummy.next

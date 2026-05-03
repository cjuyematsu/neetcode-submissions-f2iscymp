# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode(None)
        dummy = cur
        carry = 0

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            digit = l1_val + l2_val + carry

            if digit >= 10:
                carry = 1
                digit -= 10
            else:
                carry = 0

            cur.next = ListNode(digit)

            if l1 and l2:
                l1 = l1.next
                l2 = l2.next   

            elif l1:
                l1 = l1.next
            
            else:
                l2 = l2.next
            
            cur = cur.next

        if carry == 1:
            cur.next = ListNode(1)

        return dummy.next





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry != 0:
            l1Val, l2Val = 0, 0
            if l1 is not None:
                l1Val = l1.val
            if l2 is not None:
                l2Val = l2.val
            
            value = l1Val + l2Val + carry
            initValue = value
            if value >= 10:
                value = value % 10
            
            dummy.next = ListNode()
            dummy.next.val = value
            dummy = dummy.next
            carry = initValue // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return curr.next
            

        
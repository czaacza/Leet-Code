# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = list1
        curr2 = list2
        
        i = ListNode()
        res = i
        
        while curr1 and curr2:
            if curr1.val < curr2.val:
                value = curr1.val
                curr1 = curr1.next
            else:
                value = curr2.val
                curr2 = curr2.next
               
            newNode = ListNode(value)
            i.next = newNode
            i = i.next
        
        while curr1:
            newNode = ListNode(curr1.val)
            i.next = newNode
            i = i.next
            curr1 = curr1.next
        
        while curr2:
            newNode = ListNode(curr2.val)
            i.next = newNode
            i = i.next
            curr2 = curr2.next
            
        return res.next
                
            
        
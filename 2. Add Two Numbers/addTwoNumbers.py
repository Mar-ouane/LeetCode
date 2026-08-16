# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        carry = 0
        sum = 0
        while l1 != None or l2 != None or carry !=0 :
            curr.next = ListNode()
            curr = curr.next
            v1 = l1.val if l1 != None else 0
            v2 = l2.val if l2 != None else 0

            total = (v1 + v2 + carry )
           
            sum = total % 10
            carry = total // 10
            
            curr.val = sum

            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None

            
            
        return head.next


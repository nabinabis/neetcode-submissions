# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return head
        if head.next is None:
            return head
            
        else:
            prev = None
            current = head

            while current is not None:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            return prev
                
    
        


    
        #tak the first elemnt and put it in a new list then prepend the next elemnt to the new list
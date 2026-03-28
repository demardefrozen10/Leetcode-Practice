# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            prev = slow

        while slow:
            nex = slow.next
            slow.next = prev
            prev = slow
            slow = nex
        
        r = prev
        l = head

        while r and l and r != l:
            if l.val != r.val:
                return False
            else:
                l = l.next
                r = r.next
        
        return True

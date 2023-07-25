# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        root = ListNode(0)
        result = root
        toDelete = 0
        while l1 or l2 or toDelete:
            if l1:
                toDelete += l1.val
                l1 = l1.next
            if l2:
                toDelete += l2.val
                l2 = l2.next
            
            result.next = ListNode(toDelete%10)
            result = result.next
            toDelete = toDelete//10
            
        return root.next